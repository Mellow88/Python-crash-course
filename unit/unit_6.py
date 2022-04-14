"""Словники"""

alien_0 = {'color': 'green', 'point': 5, 'speed': 'medium'}

# NOTE: Додавання нових значених у словник по ключу

alien_0['position_x'] = 0
alien_0['position_y'] = 25

# NOTE: Зміна позиції відносно швидкості
alien_speed = alien_0['speed']

if alien_speed == 'slow':
    x_increment = 1
elif alien_speed == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['position_x'] = alien_0['position_x'] + x_increment

print(alien_0['color'])
print(alien_0['point'])
print(alien_0)

# NOTE: Видалення пар ключ-значення

del alien_0['speed']
print(alien_0)

# NOTE: Зверення до значення в словнику за допомогою методу get()

alien_speed = alien_0.get('speed', 'No speed')
print(alien_speed)

favourite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'c++',
}
for name in favourite_languages.keys():
    print(f"Key: {name.title()}")

# NOTE: Сортування ключів в у словнику

for name in sorted(favourite_languages.keys()):
    print(name.title())

# NOTE: Перебір значень в у словнику
# NOTE: Перевірка на унікальність елементів,
# NOTE: виконується за допомогою методу set()

for value in set(favourite_languages.values()):
    print(f"Value: {value.title()}")

# NOTE: Створення списку

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'medium'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens:
    print(alien)

# NOTE: Список у словнику

pizza = {
    'crust': 'thick',
    'topings': ['mushrooms', 'extra cheese']
}

# NOTE: Словник у словнику

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princteon',
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
        }

for username, userinfo in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
