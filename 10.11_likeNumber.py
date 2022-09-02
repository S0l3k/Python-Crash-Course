import json

likeNumber = input(f"Enter your like number! ")

filename = 'likeNumber.json'
with open(filename, 'w') as venv:
    json.dump(likeNumber, venv)
    print(f"We'll remember your like number, {likeNumber}!")
    