def show_messages(names):
    for name in names:
        message = f"Hello dear, {name.title()}, we are glad to see you!"
    return message

def send_messages(sent_message, messages):
    show_messages(message)
    current_message = message.pop()
    print(f"{current_message}")
    sent_message.append(current_message)

user = ['Tatiana', 'sasha', 'vadim', 'Ilay', 'timur']
sent_messages = []

show_messages(user)
send_messages(sent_messages, messages=show_messages())