import csv, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



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
        --=20
*AIESEC in Aachen*

Office: Elisabethstra=C3=9Fe 16 | 52056 Aachen I Tel: +49 - (0) 241 8093922
Postal Address: Templergraben 55 | 52056 Aachen
globalvolunteer.aachen@aiesec.de <lcp.aachen@aiesec.de> | www.aiesec.de

*Wir bedanken uns bei unserem F=C3=B6rderer*:
MLP
Vorsitzender des Vorstandes: Johannes-Christian Uloth
Registergericht und Registernr.: Amtsgericht Bonn, VR 8279

*National F=C3=B6rdernder Beirat von AIESEC in Deutschland:*
BASF, BearingPoint, Bertelsmann, Bosch, CLAAS, Deutsche Bahn, MLP, PHOENIX
CONTACT, Porsche, PwC, The SR Group, Vodafone, Volkswagen Nutzfahrzeuge

*Nationale Exchange Partner von AIESEC in Deutschland:*
Deutsche Post DHL Group, Deutsches Zentrum f=C3=BCr Luft- und Raumfahrt, Ro=
che
Diagnostics, trivago

*Besondere Partner von AIESEC in Deutschland:*
AIESEC Alumni Germany, Ausw=C3=A4rtiges Amt, Bundesministerium f=C3=BCr Bil=
dung und
Forschung, dasTraining, Exact Online, Management Akademie NRW, Neuland &
Partner, TeachFirst Deutschland, trendence

--0000000000005acefa05a4083f3d
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr">Sehr geehrte Frau Soldwi=
sch,<br><br>die winzigen, nur 160 Nanometer gro=C3=9Fen SARS-CoV2-Viren hab=
en bislang nicht nur zahlreiche Menschenleben gefordert, sondern unser alle=
r Leben geh=C3=B6rig durcheinander gewirbelt.=C2=A0<br><br>Als die weltweit=
 gr=C3=B6=C3=9Fte Studentenorganisation steht AIESEC nicht nur f=C3=BCr int=
erkulturellen Austausch, aber auch f=C3=BCr aktive Freiwilligenarbeit, die =
nicht nur das Leben vielerlei Menschen im Ausland ver=C3=A4ndert, sondern u=
nseren Studierenden eine M=C3=B6glichkeit bietet eine neue Seite von sich s=
elbst zu entdecken.<br>Da wir gerade keine solche Projekte hervorheben k=C3=
=B6nnen, was auch aus medizinischer Sicht erforderlich ist, m=C3=B6chten wi=
r die Studierende zu einem Online Webinar einladen.<br><br>Als junge Studie=
rende f=C3=A4llt uns =C3=B6fters schwer eine Auslandsreise zu finanzieren, =
da diese meistens mit hoher Kosten kommen. In dem Webinar m=C3=B6chten wir =
gerne den Studierenden =C3=BCber die verschiedenste Unterst=C3=BCtzungen er=
z=C3=A4hlen.<br>Dementsprechend f=C3=A4nden wir es sehr lieb wenn Sie uns i=
n Ihrer Online-Vorlesung vorstellen bzw. in Ihrem Moodle-Lernraum einen kle=
inen Beitrag =C3=BCber uns ver=C3=B6ffentlichen k=C3=B6nnten.<br><br>Den We=
binar finden Sie unter:=C2=A0<a href=3D"https://www.eventbrite.de/e/wie-du-=
deinen-auslandsaufenthalt-finanzierst-mit-aiesec-registrierung-103355039706=
" target=3D"_blank">https://www.eventbrite.de/e/wie-du-deinen-auslandsaufen=
thalt-finanzierst-mit-aiesec-registrierung-103355039706=C2=A0=C2=A0</a><br>=
<br>Mit freundlichen Gr=C3=BC=C3=9Fen,<br><br>Leonardo da Matta</div></div>=
<div><br></div>-- <br><div dir=3D"ltr" class=3D"gmail_signature" data-smart=
mail=3D"gmail_signature"><div dir=3D"ltr"><div><div dir=3D"ltr"><div><div d=
ir=3D"ltr"><div><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=
=3D"ltr"><div dir=3D"ltr"><div><div style=3D"color:rgb(80,0,80);font-size:1=
2.8px"><font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><b>AIE=
SEC in Aachen</b></font></div><div style=3D"color:rgb(80,0,80);font-size:12=
.8px"><font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><img sr=
c=3D"https://docs.google.com/uc?export=3Ddownload&amp;id=3D15ZP8qjnXDAc0ai5=
b2wAbAnPJwxOQoJ_j&amp;revid=3D0B89CAfykdVMUb1lHcERTcXNjL3ZGaUR4NWJEU1dpWUZz=
d0xJPQ" width=3D"96" height=3D"31"><br></font></div><div><div style=3D"colo=
r:rgb(80,0,80);font-size:medium"><font style=3D"color:rgb(68,68,68);font-fa=
mily:arial,helvetica,sans-serif" size=3D"1">Office: Elisabethstra=C3=9Fe 16=
 |=C2=A0</font><font style=3D"color:rgb(68,68,68);font-family:arial,helveti=
ca,sans-serif" size=3D"1">52056 Aachen I Tel:=C2=A0</font><font face=3D"ari=
al, helvetica, sans-serif" color=3D"#444444"><font size=3D"1"><a value=3D"+=
49228289800" style=3D"color:rgb(34,34,34)">+49 -</a></font></font><font fac=
e=3D"arial, helvetica, sans-serif" color=3D"#444444"><font size=3D"1"><a va=
lue=3D"+49228289800" style=3D"color:rgb(34,34,34)"><font face=3D"arial, hel=
vetica, sans-serif" color=3D"#444444"></font></a><font face=3D"arial, helve=
tica, sans-serif" color=3D"#444444"><a value=3D"+49228289800" style=3D"colo=
r:rgb(34,34,34)">=C2=A0(0) 241 8093922</a></font>=C2=A0</font></font></div>=
<div><font style=3D"color:rgb(80,0,80);font-size:medium" face=3D"arial, hel=
vetica, sans-serif"><font size=3D"1">Postal Address:=C2=A0</font></font><fo=
nt size=3D"1" face=3D"arial, helvetica, sans-serif" color=3D"#444444">Templ=
ergraben 55 | 52056 Aachen</font></div><div style=3D"color:rgb(80,0,80)"><f=
ont size=3D"1" face=3D"arial, helvetica, sans-serif" color=3D"#444444">glob=
alvolunteer.<a href=3D"mailto:lcp.aachen@aiesec.de" style=3D"color:rgb(17,8=
5,204)" target=3D"_blank">aachen@aiesec.de</a>=C2=A0|<font>=C2=A0</font><a =
href=3D"http://www.aiesec.de/" style=3D"color:rgb(17,85,204)" target=3D"_bl=
ank">www.aiesec.de</a><br></font><br style=3D"font-size:12.8px"><div style=
=3D"font-size:12.8px"><font size=3D"1" face=3D"arial, helvetica, sans-serif=
" color=3D"#444444"><b>Wir bedanken uns bei unserem F=C3=B6rderer</b>:<br>M=
LP</font></div><div style=3D"font-size:12.8px"><font size=3D"1" face=3D"ari=
al, helvetica, sans-serif" color=3D"#444444"></font></div></div></div></div=
><div><div style=3D"font-size:medium"><div dir=3D"ltr" style=3D"color:rgb(8=
0,0,80);font-size:12.8px"><div><div dir=3D"ltr"><div dir=3D"ltr"><div dir=
=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr=
"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div =
dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"ltr"><div dir=3D"=
ltr"><div dir=3D"ltr"><div dir=3D"ltr" style=3D"font-size:13.3333px"><div><=
div style=3D"font-size:13.3333px"><div style=3D"font-size:medium"><div dir=
=3D"ltr" style=3D"font-size:12.8px"><div><span style=3D"font-size:13.3333px=
"><div style=3D"font-size:medium"><div style=3D"font-size:13.3333px"><div s=
tyle=3D"font-size:13.3333px"><div style=3D"font-size:medium"><span style=3D=
"color:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-sma=
ll">Vorsitzender des Vorstandes: Johannes-Christian Uloth</span><br></div><=
font style=3D"font-size:13.3333px" face=3D"arial, helvetica, sans-serif" co=
lor=3D"#444444"><font size=3D"1">Registergericht und Registernr.: Amtsgeric=
ht Bonn, VR 8279</font></font><div style=3D"font-size:13.3333px"><div style=
=3D"font-size:13.3333px"><font face=3D"arial, helvetica, sans-serif" color=
=3D"#444444"><br><b style=3D"font-size:x-small">National F=C3=B6rdernder Be=
irat von AIESEC in Deutschland:</b><br><font size=3D"1">BASF, BearingPoint,=
 Bertelsmann, Bosch, CLAAS, Deutsche Bahn,</font></font><span style=3D"colo=
r:rgb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica, sans-serif">=C2=
=A0MLP,=C2=A0</font></span><span style=3D"color:rgb(68,68,68);font-family:a=
rial,helvetica,sans-serif;font-size:x-small">PHOENIX CONTACT,</span><span s=
tyle=3D"font-size:13.3333px;color:rgb(68,68,68)"><font size=3D"1" face=3D"a=
rial, helvetica, sans-serif">=C2=A0Porsche</font></span><span style=3D"colo=
r:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-small">,=
</span><span style=3D"font-family:arial,helvetica,sans-serif;font-size:x-sm=
all;color:rgb(68,68,68)">=C2=A0PwC,=C2=A0</span><span style=3D"color:rgb(68=
,68,68);font-family:arial,helvetica,sans-serif;font-size:x-small">The SR Gr=
oup,</span><span style=3D"color:rgb(68,68,68);font-family:arial,helvetica,s=
ans-serif;font-size:x-small">=C2=A0Vodafone,=C2=A0</span><span style=3D"col=
or:rgb(68,68,68);font-family:arial,helvetica,sans-serif;font-size:x-small">=
Volkswagen Nutzfahrzeuge</span></div><div style=3D"font-size:13.3333px"><sp=
an style=3D"color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica,=
 sans-serif"><br></font></span></div><div style=3D"font-size:13.3333px"><sp=
an style=3D"color:rgb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica,=
 sans-serif"><b>Nationale Exchange Partner von AIESEC in Deutschland:</b></=
font></span></div><div style=3D"font-size:13.3333px"><span style=3D"color:r=
gb(68,68,68)"><font size=3D"1" face=3D"arial, helvetica, sans-serif">Deutsc=
he Post DHL Group, Deutsches Zentrum f=C3=BCr Luft- und Raumfahrt, Roche Di=
agnostics, trivago=C2=A0</font></span></div><div style=3D"font-size:13.3333=
px"><span style=3D"color:rgb(68,68,68);font-family:arial,helvetica,sans-ser=
if;font-size:x-small"><br></span></div><div style=3D"font-size:13.3333px"><=
font face=3D"arial, helvetica, sans-serif" color=3D"#444444"><b style=3D"fo=
nt-size:x-small">Besondere Partner von AIESEC in Deutschland:</b><br><font =
size=3D"1">AIESEC Alumni Germany, Ausw=C3=A4rtiges Amt, Bundesministerium f=
=C3=BCr Bildung und Forschung, dasTraining,</font></font><font style=3D"fon=
t-size:13.3333px" face=3D"arial, helvetica, sans-serif" color=3D"#444444"><=
font size=3D"1">=C2=A0Exact Online,=C2=A0</font></font><span style=3D"font-=
size:x-small;color:rgb(68,68,68);font-family:arial,helvetica,sans-serif">Ma=
nagement Akademie NRW, Neuland &amp; Partner, TeachFirst Deutschland, trend=
ence</span></div><div><span style=3D"font-size:x-small;color:rgb(68,68,68);=
font-family:arial,helvetica,sans-serif"><br></span></div></div></div></div>=
</div></span></div></div></div></div></div></div></div></div></div></div></=
div></div></div></div></div></div></div></div></div></div></div></div></div=
></div></div></div></div></div></div></div></div></div></div></div></div></=
div></div></div></div></div>

--0000000000005acefa05a4083f3d--

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
                message.attach(MIMEText(text.format(receiver=name, sender=sender_name), "plain"))
                message.attach(MIMEText(html.format(receiver=name, sender=sender_name), "html"))
                message.attach(MIMEText(signature, "html"))
                server.sendmail(sender_email, email, message.as_string())
                print("Email sent to " + email)
   

if __name__ == "__main__":
    main()