"""HW_6"""

people = []

for value in range(3):
    if value == 0:
        first_name = 'ihor'
        last_name = 'sereda'
        age = '34'
        city = 'lviv'
    elif value == 1:
        first_name = 'nataly'
        last_name = 'sereda'
        age = '30'
        city = 'gorodok'
    elif value == 2:
        first_name = 'olha'
        last_name = 'sereda'
        age = '4'
        city = 'lviv'

    person_file = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'city': city,
        }
    people.append(person_file)

for person in people:
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    print('\n')

# for key, value in person_file.items():
#     if type(value) == str:
#         print(person_file.get(key).title())
#     else:
#         print(person_file.get(key))

favorite_places = {
    'ihor': ['lviv', 'radekhiv'],
    'nataly': ['lviv', 'warzaw'],
    'olha': ['lviv'],
}

for person, place in favorite_places.items():
    for place_index in place:
        print(f"For person: {person.title()}",
              f" favorive place - {place_index.title()}")
    print('\n')

favorite_numbers = {
    'nata': 1,
    'sasha': 2,
    'oleksiy': 3,
    'jonny': 4,
    'jimmy': 5,
}

for key, value in favorite_numbers.items():
    print(f"Person: {key.title()}, number: {favorite_numbers.get(key)}")
