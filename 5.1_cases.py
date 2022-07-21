#1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
#2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#3
number = [1, 3, 4, 6]
other_number = number[:]
print("\nIs number == other_number? I predict True.")
print(number == other_number)
#4
print("\nIs number == '5'? I predict False.")
print(number == 5)
#5
print("\nIs number[2] == '5-1'? I predict True.")
print(number[2] == 5-1)
#6
print("\nIs number[0] >= '5'? I predict False.")
print(number[0] >= 5)
#7
print("\nIs sum(number) == 12? I predict True.")
print(sum(number) == 14)
#8
print("\nIs len(number) >= 5? I predict False.")
print(len(number) >= 5)
#9
print("\nIs len(number)*number[0] == len(number)? I predict True.")
print(len(number)*number[0] == len(number))
#10
print("\nIs car == 'ferrari'? I predict False.")
print(car == "ferrari")