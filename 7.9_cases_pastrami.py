sandwich_order = ['Chicken Sandwich', 'pastrami', 'Egg Sandwich',
                  'Seafood Sandwich','Roast Beef Sandwich', 'Grilled Cheese',
                  'pastrami', 'Ham Sandwich','pastrami',
                  'Nutella Sandwich', 'Grilled Chicken Sandwich']
finished_sandwiches = []

print(sandwich_order)
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print(sandwich_order)

while sandwich_order:
    order = sandwich_order.pop()

    print(f"\nI made for you this sandwiches: {order.title()}")
    finished_sandwiches.append(order)

print("\nSandwiches has been done:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title())