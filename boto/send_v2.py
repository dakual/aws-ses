import smtplib, os, boto3

from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from botocore.exceptions import ClientError

SUBJECT           = "An example of Amazon SES"
SENDER            = "Daghan <daghan.altunsoy@gmail.com>"
RECIPIENT         = "daghan.altunsoy@gmail.com"
FILE_NAME         = "koala.jpg"
CHARSET           = "utf-8"
CONFIGURATION_SET = "ConfigSet"

message = MIMEMultipart("alternative")
message["From"] = SENDER
message["To"] = RECIPIENT
message["Subject"] = SUBJECT

# write the TEXT and HTML part
BODY_TEXT = "This is an example of how you can send a message in attachment with Aws SES"
BODY_HTML = """\
<html>
 <body>
   <h3>Amazon SES Demo</h3>
   <img src="cid:mailwithimage">
 </body>
</html>
"""

textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

message.attach(textpart)
message.attach(htmlpart)

# Add image
fp    = open(FILE_NAME, 'rb')
image = MIMEImage(fp.read())
fp.close()
image.add_header('Content-ID', '<mailwithimage>')
message.attach(image)

# send email
try:
  client   = boto3.client('ses')
  response = client.send_raw_email(
    Source = SENDER,
    Destinations = [ RECIPIENT ],
    RawMessage = {
        'Data':message.as_string(),
    }
  )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
