import json

def get_stored_username():
     """Получает хранимое имя пользователя, если оно существует."""

     filename = 'username.json'
     try:
         with open(filename) as venv:
             username = json.load(venv)
     except FileNotFoundError:
             return None
     else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as venv:
        json.dump(username, venv)
    return username

def greet_user():
    """Приветствует пользователя по имени."""

    cheack = input(f"Cheack name, enter name ")
    username = get_stored_username()
    if cheack != username:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
