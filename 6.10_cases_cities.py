cities = {
    'moscow': {
        'country': 'Russia',
        'population': 11_920_000,
        'fact': 'Многонациональный город на Москве-реке в западной части '
                  'страны. В его историческом центре находится средневековая'
                  ' крепость Кремль – резиденция российского президента.'},

    'paris': {
        'country': 'France',
        'population': 2_161_000,
        'fact': 'V округ Парижа, также известный как Латинский квартал, – '
                 'район, в котором находится Сорбонна и студенческие кафе. '
                 'На его территории располагаются книжные магазины, '
                 'включая знаменитый "Шекспир и Компания".'},

    'tokoy': {
        'country': 'Japane',
        'population': 13_960_000,
        'fact': 'Шумный город, в котором современные небоскребы '
                 'с неоновой подсветкой сочетаются с традиционными храмами.'}
}

for city, city_info in cities.items():
    print(f"\nCity:", city.title())
    country = f"Country is {city_info['country']}"
    population = f"Population in {city.title()} is {city_info['population']}"
    fact = f"Fact about {city.title()} : {city_info['fact']}"
    print("\t", country)
    print("\t", population)
    print("\t", fact)