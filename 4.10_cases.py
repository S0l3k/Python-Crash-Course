numbers = []
for value in range(1,11):
    numbers.append(value**3)
print(numbers)
print(sum(numbers))

print("The irst three numbers in the list are:", numbers[:3])
print("Three items from the middle of the list are:", numbers[3:6])
print("The last three items in the list are:", numbers[-3:])