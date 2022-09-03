import json

def get_like_number():
    """Get a like number of user, if he is do"""

    filename = 'likeNumber.json'
    try:
        with open(filename) as venv:
            likeNumber = json.load(venv)
    except FileNotFoundError:
        return None
    else:
        return likeNumber

def enter_like_number():
    """Show like number of user"""

    likeNumber = get_like_number()
    if likeNumber:
        print(f"Your like number is {likeNumber}!")
    else:
        likeNumber = input(f"Enter your like number! ")
        filename = "likeNumber.json"
        with open(filename, 'w') as venv:
            json.dump(likeNumber, venv)
            print(f"We'll remember your like number, {likeNumber}!")

enter_like_number()