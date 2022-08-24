from random import choice

values = [23, 83, 2, 94, 49, 36, 42, 73, 92, 9,
          'win', 'love', 'lose', 'bet', 'millioner']
n = 0
winner = []
while n <= 3:
    win_ticket = choice(values)
    winner.append(win_ticket)
    n += 1

print('If you have in ticket that values', winner)