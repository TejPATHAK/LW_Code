from twilio.rest import Client

def send_sms(to_number, message):
    
    account_sid = 'AC3198ce289a5fbf990bda53f94208815d'
    auth_token = '2673af9e7c3412f0acff3a3e9358dfff'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        to=to_number, 
        from_="+1234567890",  # Twilio number
        body=message)
    
    print(f"Message sent to {to_number}")

# Example usage:
send_sms("+919356563105", "Hello from Python!")
