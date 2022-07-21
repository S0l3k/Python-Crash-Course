cars = ['audi', 'mersedes', 'tayota', 'subaru', 'kia', 'honda']
print(cars)

#sort() сортировка от А до Я

cars.sort()
print(cars, 'A - Z')

#sort(reverse=True) сортировка от Я до А

cars.sort(reverse=True)
print(cars, 'Z - A')

#sorted() временная сортировка от А до Я

cars = ['audi', 'mersedes', 'tayota', 'subaru', 'kia', 'honda']
print('\nList not sorted', cars)
print('Sorted list A-Z', sorted(cars))
print('Sorted list Z-A', sorted(cars,reverse=True))
print('List again not sorted', cars)

#revers() перестановка элеметов с конца в начало

cars = ['audi', 'mersedes', 'tayota', 'subaru', 'kia', 'honda']
print(cars)
cars.reverse()
print(cars)

#len() определение длины списка

cars = ['audi', 'mersedes', 'tayota', 'subaru', 'kia', 'honda']
print(len(cars))