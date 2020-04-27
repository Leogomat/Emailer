import csv, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from quopri import decodestring


def main():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "damatta.developer@gmail.com"
    subject = "hello"
    password = "Saegl0pur"
    sender_name = "leo"

    text = """\
    Hello {receiver},

    click the following link: google.com

    Best regards,
    {sender}"""

    

    html = """\
    <html>
        <body>
            <p> Hello {receiver}<br>
                click the following link: <a href="google.com">google.com</a><br>
                Best regards,<br>
                {sender}
            </p>
            
        </body>
        
    </html>
    """

    signature = """\
<div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr">Sehr geehrte=C2=A0 Frau =
Wiese,<br><br>die winzigen, nur 160 Nanometer gro=C3=9Fen SARS-CoV2-Viren h=
aben bislang nicht nur zahlreiche Menschenleben gefordert, sondern unser al=
ler Leben geh=C3=B6rig durcheinander gewirbelt.=C2=A0<br><br>Als die weltwe=
it gr=C3=B6=C3=9Fte Studentenorganisation steht AIESEC nicht nur f=C3=BCr i=
nterkulturellen Austausch, aber auch f=C3=BCr aktive Freiwilligenarbeit, di=
e nicht nur das Leben vielerlei Menschen im Ausland ver=C3=A4ndert, sondern=
 unseren Studierenden eine M=C3=B6glichkeit bietet eine neue Seite von sich=
 selbst zu entdecken.<br>Da wir gerade keine solche Projekte hervorheben k=
=C3=B6nnen, was auch aus medizinischer Sicht erforderlich ist, m=C3=B6chten=
 wir die Studierende zu einem Online Webinar einladen.<br><br>Als junge Stu=
dierende f=C3=A4llt uns =C3=B6fters schwer eine Auslandsreise zu finanziere=
n, da diese meistens mit hoher Kosten kommen. In dem Webinar m=C3=B6chten w=
ir gerne den Studierenden =C3=BCber die verschiedenste Unterst=C3=BCtzungen=
 erz=C3=A4hlen.<br>Dementsprechend f=C3=A4nden wir es sehr lieb wenn Sie un=
s in Ihrer Online-Vorlesung vorstellen bzw. in Ihrem Moodle-Lernraum einen =
kleinen Beitrag =C3=BCber uns ver=C3=B6ffentlichen k=C3=B6nnten.<br><br>Den=
 Webinar finden Sie unter:=C2=A0<a href=3D"https://www.eventbrite.de/e/wie-=
du-deinen-auslandsaufenthalt-finanzierst-mit-aiesec-registrierung-103355039=
706" target=3D"_blank">https://www.eventbrite.de/e/wie-du-deinen-auslandsau=
fenthalt-finanzierst-mit-aiesec-registrierung-103355039706=C2=A0=C2=A0</a><=
br><br>Mit freundlichen Gr=C3=BC=C3=9Fen,<br><br>Buse Karag=C3=B6z</div></d=
iv><div><br></div>-- <br><div dir=3D"ltr" class=3D"gmail_signature" data-sm=
artmail=3D"gmail_signature"><div dir=3D"ltr"><div><div dir=3D"ltr"><div><di=
v dir=3D"ltr"><div><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div =
dir=3D"ltr"><div dir=3D"ltr"><div><div style=3D"color:rgb(80,0,80);font-siz=
e:12.8px"><font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><b>=
AIESEC in Aachen</b></font></div><div style=3D"color:rgb(80,0,80);font-size=
:12.8px"><font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><img=
 src=3D"https://docs.google.com/uc?export=3Ddownload&amp;id=3D15ZP8qjnXDAc0=
ai5b2wAbAnPJwxOQoJ_j&amp;revid=3D0B89CAfykdVMUb1lHcERTcXNjL3ZGaUR4NWJEU1dpW=
UZzd0xJPQ" width=3D"96" height=3D"31"><br></font></div><div><div style=3D"c=
olor:rgb(80,0,80);font-size:medium"><font style=3D"color:rgb(68,68,68);font=
-family:arial,helvetica,sans-serif" size=3D"1">Office: Elisabethstra=C3=9Fe=
 16 |=C2=A0</font><font style=3D"color:rgb(68,68,68);font-family:arial,helv=
etica,sans-serif" size=3D"1">52056 Aachen I Tel:=C2=A0</font><font face=3D"=
arial, helvetica, sans-serif" color=3D"#444444"><font size=3D"1"><a value=
=3D"+49228289800" style=3D"color:rgb(34,34,34)">+49 -</a></font></font><fon=
t face=3D"arial, helvetica, sans-serif" color=3D"#444444"><font size=3D"1">=
<a value=3D"+49228289800" style=3D"color:rgb(34,34,34)"><font face=3D"arial=
, helvetica, sans-serif" color=3D"#444444"></font></a><font face=3D"arial, =
helvetica, sans-serif" color=3D"#444444"><a value=3D"+49228289800" style=3D=
"color:rgb(34,34,34)">=C2=A0(0) 241 8093922</a></font>=C2=A0</font></font><=
/div><div><font style=3D"color:rgb(80,0,80);font-size:medium" face=3D"arial=
, helvetica, sans-serif"><font size=3D"1">Postal Address:=C2=A0</font></fon=
t><font size=3D"1" face=3D"arial, helvetica, sans-serif" color=3D"#444444">=
Templergraben 55 | 52056 Aachen</font></div><div style=3D"color:rgb(80,0,80=
)"><font size=3D"1" face=3D"arial, helvetica, sans-serif" color=3D"#444444"=
>globalvolunteer.<a href=3D"mailto:lcp.aachen@aiesec.de" style=3D"color:rgb=
(17,85,204)" target=3D"_blank">aachen@aiesec.de</a>=C2=A0|<font>=C2=A0</fon=
t><a href=3D"http://www.aiesec.de/" style=3D"color:rgb(17,85,204)" target=
=3D"_blank">www.aiesec.de</a><br></font><br style=3D"font-size:12.8px"><div=
 style=3D"font-size:12.8px"><font size=3D"1" face=3D"arial, helvetica, sans=
-serif" color=3D"#444444"><b>Wir bedanken uns bei unserem F=C3=B6rderer</b>=
:<br>MLP</font></div><div style=3D"font-size:12.8px"><font size=3D"1" face=
=3D"arial, helvetica, sans-serif" color=3D"#444444"></font></div></div></di=
v></div><div><div style=3D"font-size:medium"><div dir=3D"ltr" style=3D"colo=
r:rgb(80,0,80);font-size:12.8px"><div><div dir=3D"ltr"><div dir=3D"ltr"><di=
v dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=
=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr=
"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div =
dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr" style=3D"font-size:13.3333px"=
><div><div style=3D"font-size:13.3333px"><div style=3D"font-size:medium"><d=
iv dir=3D"ltr" style=3D"font-size:12.8px"><div><span style=3D"font-size:13.=
3333px"><div style=3D"font-size:medium"><div style=3D"font-size:13.3333px">=
<div style=3D"font-size:13.3333px"><div style=3D"font-size:medium"><span st=
yle=3D"color:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size=
:x-small">Vorsitzender des Vorstandes: Johannes-Christian Uloth</span><br><=
/div><font style=3D"font-size:13.3333px" face=3D"arial, helvetica, sans-ser=
if" color=3D"#444444"><font size=3D"1">Registergericht und Registernr.: Amt=
sgericht Bonn, VR 8279</font></font><div style=3D"font-size:13.3333px"><div=
 style=3D"font-size:13.3333px"><font face=3D"arial, helvetica, sans-serif" =
color=3D"#444444"><br><b style=3D"font-size:x-small">National F=C3=B6rdernd=
er Beirat von AIESEC in Deutschland:</b><br><font size=3D"1">BASF, BearingP=
oint, Bertelsmann, Bosch, CLAAS, Deutsche Bahn,</font></font><span style=3D=
"color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica, sans-serif=
">=C2=A0MLP,=C2=A0</font></span><span style=3D"color:rgb(68,68,68);font-fam=
ily:arial,helvetica,sans-serif;font-size:x-small">PHOENIX CONTACT,</span><s=
pan style=3D"font-size:13.3333px;color:rgb(68,68,68)"><font size=3D"1" face=
=3D"arial, helvetica, sans-serif">=C2=A0Porsche</font></span><span style=3D=
"color:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-sma=
ll">,</span><span style=3D"font-family:arial,helvetica,sans-serif;font-size=
:x-small;color:rgb(68,68,68)">=C2=A0PwC,=C2=A0</span><span style=3D"color:r=
gb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-small">The =
SR Group,</span><span style=3D"color:rgb(68,68,68);font-family:arial,helvet=
ica,sans-serif;font-size:x-small">=C2=A0Vodafone,=C2=A0</span><span style=
=3D"color:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-=
small">Volkswagen Nutzfahrzeuge</span></div><div style=3D"font-size:13.3333=
px"><span style=3D"color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, hel=
vetica, sans-serif"><br></font></span></div><div style=3D"font-size:13.3333=
px"><span style=3D"color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, hel=
vetica, sans-serif"><b>Nationale Exchange Partner von AIESEC in Deutschland=
:</b></font></span></div><div style=3D"font-size:13.3333px"><span style=3D"=
color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica, sans-serif"=
>Deutsche Post DHL Group, Deutsches Zentrum f=C3=BCr Luft- und Raumfahrt, R=
oche Diagnostics, trivago=C2=A0</font></span></div><div style=3D"font-size:=
13.3333px"><span style=3D"color:rgb(68,68,68);font-family:arial,helvetica,s=
ans-serif;font-size:x-small"><br></span></div><div style=3D"font-size:13.33=
33px"><font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><b styl=
e=3D"font-size:x-small">Besondere Partner von AIESEC in Deutschland:</b><br=
><font size=3D"1">AIESEC Alumni Germany, Ausw=C3=A4rtiges Amt, Bundesminist=
erium f=C3=BCr Bildung und Forschung, dasTraining,</font></font><font style=
=3D"font-size:13.3333px" face=3D"arial, helvetica, sans-serif" color=3D"#44=
4444"><font size=3D"1">=C2=A0Exact Online,=C2=A0</font></font><span style=
=3D"font-size:x-small;color:rgb(68,68,68);font-family:arial,helvetica,sans-=
serif">Management Akademie NRW, Neuland &amp; Partner, TeachFirst Deutschla=
nd, trendence</span></div><div><span style=3D"font-size:x-small;color:rgb(6=
8,68,68);font-family:arial,helvetica,sans-serif"><br></span></div></div></d=
iv></div></div></span></div></div></div></div></div></div></div></div></div=
></div></div></div></div></div></div></div></div></div></div></div></div></=
div></div></div></div></div></div></div></div></div></div></div></div></div=
></div></div></div></div></div></div>

    """

    
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        with open("data.csv") as data:
            reader = csv.reader(data)
            for email, name, gender in reader:
                message = MIMEMultipart("alternative")
                message["Subject"] = subject
                message["From"] = sender_email
                message["To"] = email
                #message.attach(MIMEText(text.format(receiver=name, sender=sender_name), "plain"))
                #message.attach(MIMEText(html.format(receiver=name, sender=sender_name), "html"))
                message.attach(MIMEText(decodestring(signature).decode("utf-8"), "html"))
                server.sendmail(sender_email, email, message.as_string())
                print("Email sent to " + email)
   

if __name__ == "__main__":
    main()