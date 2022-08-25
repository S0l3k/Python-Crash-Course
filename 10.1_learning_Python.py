with open('learning_python.txt') as venv:
    n = 0
    while n <= 2:
        contents = venv.read()
        print(contents)
        print('\n', contents)
        print('\n', contents)
        n += 1