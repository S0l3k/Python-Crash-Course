def show_messages(names, sent_message):
    while user:
        current_message = user.pop()
        message = f"Hello dear, {current_message.title()}, we are glad to see you!"
        sent_messages.append(message)

def send_messages(sent_messages):
    for sent_messages in sent_messages:
        current_message = f"\n{sent_messages}"
        print(current_message)

user = ['Tatiana', 'sasha', 'vadim', 'Ilay', 'timur']
sent_messages = []

show_messages(user, sent_messages)
send_messages(sent_messages)
send_messages(sent_messages[:])

print("\n")
print(sent_messages)
print("\n")
print(sent_messages[:])
