from twilio.rest import Client

# Your Twilio credentials
account_sid = 'AC3198ce289a5fbf990bda53f94208815d'
auth_token = '2673af9e7c3412f0acff3a3e9358dfff'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send an SMS
message = client.messages.create(
    body="Hello, this is a test message!",  # The content of the SMS
    from_='++12532001832',                    # Your Twilio phone number
    to='+919356563105'                        # The recipient's phone number
)

# Print the message SID (useful for tracking the message)
print(f"Message sent! Message SID: {message.sid}")
