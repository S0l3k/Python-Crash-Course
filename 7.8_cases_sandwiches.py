sandwich_order = ['Chicken Sandwich', 'Egg Sandwich', 'Seafood Sandwich',
                  'Roast Beef Sandwich', 'Grilled Cheese', 'Ham Sandwich',
                  'Nutella Sandwich', 'Grilled Chicken Sandwich']
finished_sandwiches = []

while sandwich_order:
    order = sandwich_order.pop()

    print(f"I made for you this sandwiches: {order.title()}")
    finished_sandwiches.append(order)

print("\nSandwiches has been done:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title())