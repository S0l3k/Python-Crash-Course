people = []

person = {'first_name': 'sasha',
                     'last_name': 'vodolazskay',
                     'age': 24,
                     'city': 'moscow'
                    }
people.append(person)

person = {'first_name': 'vadim',
                     'last_name': 'novikov',
                     'age': 21,
                     'city': 'moscow'
                     }
people.append(person)

person = {'first_name': 'ilay',
                    'last_name': 'saprohin',
                    'age': 21,
                    'city': 'moscow'
                    }
people.append(person)


    #for key, value in sasha_information.items():
    #    full_name = f"{sasha_information['first_name']} {sasha_information['last_name']}"
    #    age = f"{sasha_information['age']}"
    #    city = f"{sasha_information['city']}"
    #    print("\nFull name:", full_name.title())
    #    print("Age :", age)
    #    print("Location :", city.title())

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name} from {city} is {age} years old.")