try:
    f_number = int(input(f"Введите 1-ое число: "))
except ValueError:
    print("First number doesn't integer!")
try:
    s_number = int(input(f"Введите 2-ое число: "))
except ValueError:
    print("Second number doesn't integer!")
try:
    addition = f_number + s_number
except NameError:
    print("One of numbers doesn't integer!")
    addition = 'None'
print(addition)