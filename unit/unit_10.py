"""Файли та винятки"""

import json

# NOTE: Читання з файлу
file_name = 'text_files/pi_digits.txt'

with open(file_name, encoding="utf8") as file_object:
    contents = file_object.read()

print(contents.rstrip())
print('\t')

# NOTE: Зчитування файлу рядок за рядком
with open(file_name, encoding="utf8") as file_object:
    for line in file_object:
        print(line.rstrip())

print('\t')

# NOTE: Створення списку рядків на базі файлу
with open(file_name, encoding="utf8") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print('\t')

# NOTE: РОбота з вмістом файлу
pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print('\t')

# NOTE: Великі файли: мільйон цифр
pi_string = ''

with open('text_files/pi_million_digits.txt', encoding="utf8") as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

if '120372' in pi_string:
    print('yes')

# NOTE: Запис у файл
# NOTE: При записі даних у файл, дані перезаписуються
file_name = 'text_files/programming.txt'

with open(file_name, 'w', encoding="utf8") as file_object:
    file_object.write('I love python!\n')
    file_object.write('Add record\n')

print('\t')

# NOTE: Додавання у файл нової інформації
with open(file_name, 'a', encoding="utf8") as file_object:
    file_object.write('I also love C++')

# NOTE: Винятки
try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by zero')

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

print('\t')

file_name = 'text_files/alice.txt'

try:
    with open(file_name, encoding="utf8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")

# NOTE: Зберігання даних у формат  JSON
file_name = 'text_files/numbers.json'
numbers = [1, 2, 2, 3, 23, 432]

with open(file_name, 'w', encoding="utf8") as f:
    json.dump(numbers, f)

# NOTE: Зчитування даних JSON
with open(file_name, encoding="utf8") as f:
    num_list = json.load(f)

print(num_list)

# NOTE: Збереження та читання користувацьких даних
def get_stored_username():
    """Get stored username if available."""
    filename = 'text_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'text_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
