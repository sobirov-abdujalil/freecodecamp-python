# Workshop: Build an Email Simulator
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.sent = False

    def send(self):
        self.sent = True
        return f"Email sent from {self.sender} to {self.recipient}"

class Inbox:
    def __init__(self):
        self.emails = []

    def receive(self, email):
        self.emails.append(email)

    def unread_count(self):
        return sum(1 for e in self.emails if not e.sent)
