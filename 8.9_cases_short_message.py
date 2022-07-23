def show_messages(names):
    for name in names:
        message = f"Hello dear, {name.title()}, we are glad to see you!"
        print(message)

user = ['Tatiana', 'sasha', 'vadim', 'Ilay', 'timur']
show_messages(user)