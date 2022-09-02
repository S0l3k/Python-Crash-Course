import json

filename = 'likeNumber.json'
try:
    with open(filename) as venv:
        likeNumber = json.load(venv)
except FileNotFoundError:
    print(f"The {filename}   doesn't in this directory")
else:
    print(f"I member your like number, it's {likeNumber}")