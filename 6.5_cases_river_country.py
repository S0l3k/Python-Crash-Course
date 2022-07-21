river_country = {'volga': 'russia',
                 'dunay': 'germany',
                 'ural': 'kazakhstan',
                 'dnieper': 'ukraine',
                 'dniester': 'moldova'}

for river, country in river_country.items():
    print(f"\nThe {river.title()} runs trought {country.title()}.")
for river in river_country.keys():
    print("\n\t", river.title())
for country in river_country.values():
    print("\n\t\t", country.title())
