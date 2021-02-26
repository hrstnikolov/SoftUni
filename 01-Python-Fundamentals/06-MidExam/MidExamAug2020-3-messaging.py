class Chat:
    def __init__(self):
        self.messages = []

    def chat(self, msg):
        self.messages.append(msg)

    def delete(self, msg):
        if msg in self.messages:
            self.messages.remove(msg)

    def edit(self, msg, edited_msg):
        for ind, m in enumerate(self.messages):
            if msg == m:
                self.messages[ind] = edited_msg
                break

    def pin(self, msg):
        if msg in self.messages:
            self.messages.remove(msg)
            self.messages.append(msg)

    def spam(self, msgs):
        for msg in msgs:
            self.messages.append(msg)

    def __repr__(self):
        return '\n'.join(self.messages)


my_chat = Chat()

while True:
    line = input()
    if line == 'end':
        break

    commands = line.split(' ')
    action = commands[0]

    if action == 'Chat':
        msg = commands[1]
        my_chat.chat(msg)
    if action == 'Delete':
        msg = commands[1]
        my_chat.delete(msg)
    if action == 'Edit':
        msg = commands[1]
        edited_msg = commands[2]
        my_chat.edit(msg, edited_msg)
    if action == 'Pin':
        msg = commands[1]
        my_chat.pin(msg)
    if action == 'Spam':
        msgs = commands[1:]
        my_chat.spam(msgs)

print(my_chat)