filename = 'answer.txt'

print("Enter 'quit' when are you finished.")
while True:
    answer = input('\nWhy are you like program? ')
    if answer == 'quit':
        break
    else:
        with open('answer.txt', 'a') as venv:
            venv.write(f"{answer}\n")