"""Користувацький ввід та цикл WHILE"""

# NOTE: Функція input()
message = input('Tell me someshing, and I will repeat it back to you: ')
print(message)

# NOTE: Додавання до стрічки даних
TEXT = 'exemple'
TEXT += ' word'
print(TEXT)

age = input('How old are you? ')
age = int(age)

if age >= 18:
    print('You are adulter')
else:
    print('You are so young')

# NOTE: Цикл while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# NOTE: Використання булевої змінної
promt = '\nTell me something about for you:'
promt += "\tEnter 'quit' to end program "

active = True

while active:
    message = input(promt)
    if message == 'quit':
        active = False
        # NOTE: Вихід з циклу
        # break
    else:
        print(message)

# Почати з користувачів, яких треба перевірити,
# та порожнього списку підтверджених користувачів
uncormfirmed_users = ['jonni', 'paolo', 'teddy']
confirmed_users = []

while uncormfirmed_users:
    current_user = uncormfirmed_users.pop()
    print(f"Verify user: {current_user.title()}")
    confirmed_users.append(current_user)

# NOTE: Видалення значень зі списку
pets = ['cat', 'dog', 'cat', 'rabbit', 'goldfish', 'cat', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
