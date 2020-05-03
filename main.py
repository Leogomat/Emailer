import csv, smtplib, ssl, configurations, os
from email import message_from_file
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from quopri import decodestring


def main():

    # Input gmail account password
    password = input("Password: ")
    
    # Creat SSL context for sending the message
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(configurations.SMTP_SERVER, configurations.PORT, context=context) as server:
        server.login(configurations.SENDER_EMAIL, password)
        with open(configurations.DATA) as data:
            reader = csv.reader(data)
            for gender, name, email in reader:
                with open(os.path.join(configurations.SCHEMA_PATH, configurations.SCHEMA)) as file:

                    # Declare the message object and adjust the header parameters
                    message = message_from_file(file)
                    message.replace_header("To", email)
                    message.replace_header("Message-ID", '')
                    
                    # Replace the personalizeable fields of the message with their values
                    for m in message.get_payload():
                        m.set_payload(m.get_payload().format(sender=configurations.SENDER_NAME, receiver=name, greetings=("Sehr geehrte" + ("r Herr" if gender=="Herr" else " Frau"))))

                    # Send message
                    server.send_message(message)
                    print("Email sent to " + email)
   

if __name__ == "__main__":
    main()