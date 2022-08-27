with open('learning_python.txt') as venv:
    lines = venv.readlines()

words = ''
for line in lines:
    words += line.lstrip()
print(f"{words}")

r = words.replace('Python', 'C++')
print(r)