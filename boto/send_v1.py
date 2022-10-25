import boto3

client   = boto3.client('ses')
response = client.send_email(
    Destination={
        'ToAddresses': [
            'daghan.altunsoy@gmail.com'
        ],
    },
    Message={
        'Body': {
            'Html': {
                'Charset': 'UTF-8',
                'Data': '<h1>Hello World</h1><p>This is a pretty mail with HTML formatting</p>',
            },
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is for those who cannot read HTML.',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Hello World',
        },
    },
    Source='daghan.altunsoy@gmail.com',
)

print("Email sent! Message ID:")
print(response['MessageId'])