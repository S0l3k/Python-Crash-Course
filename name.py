name = ['ílay', 'timur', 'dany', 'sasha']
print(name[0])
print(name[1].capitalize())
print(name[2].upper())
print(name[3].title())

message = f"I want to come with you, {name[0].title()}!"
print(message)
message = f"I want to come with you, {name[1].title()}!"
print(message)
message = f"I want to come with you, {name[2].title()}!"
print(message)
message = f"I want to come with you, {name[3].title()}!"
print(message)

hero_name = ['Pangolier', 'TA', 'ember spirit', 'void spirit', 'batrider']
character = ['initiator', 'physical damage', 'hand physical damage', 'magic damage', 'oil']
some_message = f"{hero_name[0].title()}, is {character[0]} !"
print(some_message)
some_message = f"{hero_name[1].title()}, is {character[1]} !"
print(some_message)
some_message = f"{hero_name[2].title()}, is {character[2]} !"
print(some_message)
some_message = f"{hero_name[3].title()}, is {character[3]} !"
print(some_message)
some_message = f"{hero_name[4].title()}, is {character[4]} !"
print(some_message)

#append() and insert()

print(hero_name)
hero_name.append("queen of pain")
print(hero_name)

hero_name.insert(2,'marci')
print(hero_name)

#del and pop()

del hero_name[2]
print(hero_name)

popend_hero_name = hero_name.pop(5)
print(hero_name)
deleted_hero = f"{popend_hero_name.title()} was deleted !"
print(deleted_hero)

#remove()

print(name)
name.remove('timur')
print(name)