vadim_n = [19, 2, 9]
sasha_n = [16, 150, 26]
timur_n = [10, 1, 300_000]
ilay_n = [29, 4, 10_000]
mom_n = [15, 8, 5]

favorite_number = {'vadim': vadim_n,
                   'sasha': sasha_n,
                   'timur': timur_n,
                   'ilay': ilay_n,
                   'mom': ilay_n}

for name, number in favorite_number.items():
    print(f"{name.title()} lover number is {number}")