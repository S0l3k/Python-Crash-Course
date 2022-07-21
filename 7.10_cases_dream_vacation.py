responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("How do you imagine your dream vacation? ")

    responses[name] = response

    repeat = input("Would you want to let another answer? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("Pool Resualts")
for name, response in responses.items():
    print(f"{name.title()} dreaming of such a holiday {response}.")