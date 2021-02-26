class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


class Mailbox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, email_indices):
        for index in email_indices:
            self.emails[index].send()

    def print_mailbox(self):
        for mail in self.emails:
            print(mail.get_info())


my_mailbox = Mailbox()

# Read emails
while True:
    line = input()
    if line == 'Stop':
        break
    sender, receiver, content = line.split(' ', maxsplit=2)

    email = Email(sender, receiver, content)
    my_mailbox.add_email(email)

# Send emails
emails_to_send = [int(_) for _ in input().split(', ')]
my_mailbox.send_emails(emails_to_send)

# Print the mail box
my_mailbox.print_mailbox()