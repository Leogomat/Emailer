import csv, smtplib, ssl, configurations, authentication, os, time
from email import message_from_file
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import quopri
import io
import pandas as pd


def to_quopri(msg):
    return quopri.encodestring(msg.encode()).decode()


def main():
    # Input gmail account password
    #password = input("Password: ")
    
    # Creat SSL context for sending the message
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(configurations.SMTP_SERVER, configurations.PORT, context=context) as server:
        
        access_token, expires_in = authentication.refresh_authorization(authentication.GOOGLE_CLIENT_ID,
                                                                        authentication.GOOGLE_CLIENT_SECRET,
                                                                        authentication.GOOGLE_REFRESH_TOKEN)
        auth_string = authentication.generate_oauth2_string(configurations.SENDER_EMAIL, access_token, as_base64=True)
        server.ehlo(authentication.GOOGLE_CLIENT_ID)
        server.docmd('AUTH', 'XOAUTH2 ' + auth_string)
        #server.login(configurations.SENDER_EMAIL, password)

        with open(configurations.DATA, encoding="utf-8") as data:
            reader = csv.reader(data)
            
            next(reader)

            count = 0
            automatic = "n"

            for gender, name, email, active, answered, pending, bwl in reader:
                with open(os.path.join(configurations.SCHEMA_PATH, configurations.SCHEMA)) as file:
                    
                    # Declare the message object and adjust the header parameters
                    message = message_from_file(file)
                    message.replace_header("From", configurations.SENDER_EMAIL)
                    message.replace_header("To", email)
                    message.replace_header("Message-ID", '')
                    
                    
                    # Replace the personalizeable fields of the message with their values
                    for m in message.get_payload()[0].get_payload(): # No need for indexing if no file attached
                        m.set_payload(m.get_payload().replace("=\n", "").format(sender=to_quopri(configurations.SENDER_NAME),
                                                             receiver=to_quopri(name),
                                                             greetings=("Sehr geehrte" + ("r Herr" if gender=="Herr" else " Frau")),
                                                             collab=(to_quopri(configurations.COLLAB_MSG) if answered.lower() == "yes" else "")))

                    

                    # Send message
                    if pending.lower() == "no" and answered.lower() == "no" and bwl.lower() == "yes":

                        # Security prompt
                        if not automatic.lower() == "y":
                            automatic = input("Continue automatically? [y/n]: ")

                        server.send_message(message)
                        count += 1
                        print("Email sent to " + email + " (%d/" % count + ")")
                        time.sleep(0.5)
   

if __name__ == "__main__":
    main()