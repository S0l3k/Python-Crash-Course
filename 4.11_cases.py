pizza = ['cheese', 'pepperonni', 'hunting']
for message in pizza:
    print('I like' , message , 'pizza !')
print('\nI really love pizza!')

friend_pizza = pizza[:]
pizza.append('arriva')
friend_pizza.append('mushrom')

print('My favorite pizzas are:')
for name in pizza:
    print(name)
print('My friend’s favorite pizzas are:')
for name in friend_pizza:
    print(name)
