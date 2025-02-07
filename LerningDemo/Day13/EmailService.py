class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send_email(message)

email_service = EmailService()
notifier = Notification(email_service)
notifier.notify("Hello, World!")
