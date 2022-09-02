try:
    filecats = 'cats.txt'
    with open(filecats, 'r') as venv:
        cats = venv.read()
        print(cats)
except FileNotFoundError:
    print("File 'cats.txt' isn't find")

try:
    filedogs = 'dogs.txt'
    with open(filedogs, 'r') as venv:
        dogs = venv.read()
        print(dogs)
except FileNotFoundError:
    print("File 'dogs.txt' isn't find")