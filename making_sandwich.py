def make_sandwich(*componets):
    """"Создает сандвичи, получая ингридиенты"""
    print(f"\nYour sandwiche have that ingridients: ")
    for componets in componets:
        print(f"\t- {componets}")