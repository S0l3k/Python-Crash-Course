nameOfGuest = input(f"Enter your name,plz ")

with open('guest.txt', 'a') as venv:
    venv.write(nameOfGuest)
    print(nameOfGuest)

