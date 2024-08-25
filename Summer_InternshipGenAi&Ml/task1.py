import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email():
    # Your SendGrid API key
    sg = SendGridAPIClient(api_key='your_sendgrid_api_key')

    # Create a Mail object
    message = Mail(
        from_email='your_email@example.com',
        to_emails='recipient_email@example.com',
        subject='Subject of the Email',
        html_content='<strong>This is the body of the email in HTML.</strong>'
    )

    try:
        # Send the email
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_email()
