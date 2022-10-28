import boto3

client   = boto3.client('ses')
response = client.verify_email_identity(
    EmailAddress = 'daghan@kruta.link'
)