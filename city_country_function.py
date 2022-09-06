def city_functions(city, country, population):
    """Строит отформатированное название Город/Страна."""

    city_country = f"{city} {country} - population {population}"

    return city_country.title()