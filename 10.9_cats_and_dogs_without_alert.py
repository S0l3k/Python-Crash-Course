try:
    filecats = 'cats.txt'
    with open(filecats, 'r') as venv:
        cats = venv.read()
        print(cats)
except FileNotFoundError:
    print("")

try:
    filedogs = 'dogs.txt'
    with open(filedogs, 'r') as venv:
        dogs = venv.read()
        print(dogs)
except FileNotFoundError:
    print("")