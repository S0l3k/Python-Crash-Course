def city_country(city, country):
    formated = f"\n{city.title()}, {country.title()}."
    return formated

f_city_country = city_country('New-York', 'USA')
print(f_city_country)