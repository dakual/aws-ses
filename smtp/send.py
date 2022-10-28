import smtplib, os

from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv(".env")

email_host     = os.environ.get("EMAIL_HOST")
email_port     = os.environ.get("EMAIL_PORT")
email_username = os.environ.get("EMAIL_USERNAME")
email_password = os.environ.get("EMAIL_PASSWORD")

subject        = "An example of python email"
sender_email   = "Daghan <daghan@kruta.link>"
receiver_email = "daghan.altunsoy@gmail.com"
filename       = "koala.jpg"

message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# write the HTML part
body = "This is an example of how you can send a message in attachment with Python"
html = """\
<html>
 <body>
   <img src="cid:mailwithimage">
 </body>
</html>
"""
message.attach(MIMEText(body, "plain"))
message.attach(MIMEText(html, "html"))


# Add image
fp    = open(filename, 'rb')
image = MIMEImage(fp.read())
fp.close()
image.add_header('Content-ID', '<mailwithimage>')
message.attach(image)

# send your email
with smtplib.SMTP(email_host, email_port) as server:
  server.starttls()
  server.login(email_username, email_password)
  server.sendmail(
      sender_email, receiver_email, message.as_string()
  )

print('Sent') 