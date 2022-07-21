text = "\nEnter a some topping, which are you want to add a pizza!"
text += "\nIf you want to leave a program, enter a 'exit'."
topping = ""

while topping != 'exit':
    print(text)
    topping = input(topping)

    if topping != 'exit':
        print("You add a pizza this topping:", topping)
