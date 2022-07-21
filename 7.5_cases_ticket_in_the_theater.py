text = "\nHow old are you?"
text += "\nIf you want to leave, enter the '999' "

while True:
    age = input(text)
    age = int(age)

    if age != 999:
        if age < 3:
            print("Enter the FREE!")
            break
        elif age >= 3 and age < 12:
            print("Ticket are cost 10$")
            break
        elif age >= 12:
            print("Ticket are cost 15$")
            break
    break