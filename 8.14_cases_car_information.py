def make_car(mark, name, **car_information):
    """Создает словарь с названием марки, модели и некоторым кол-ом параметров"""
    car_information['mark'] = mark #subaru, bmw, suzuki etc.
    car_information['model'] = name
    return car_information

car = make_car('BMW', 'E30',
               color = 'black',
               type = 'sedan')

print(car)