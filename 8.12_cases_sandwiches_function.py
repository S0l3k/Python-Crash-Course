def make_sandwich(*componets):
    print(f"\nYour sandwiche have that ingridients: ")
    for componets in componets:
        print(f"\t- {componets}")

make_sandwich('cheese', 'bread', 'salat', 'sausage')
make_sandwich('bread', 'chicken', 'cheese sauce', 'salat')
make_sandwich('bread', 'caesar sauce', 'hum', 'cucumber')