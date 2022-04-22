"""HW_10"""

import json

# NOTE: Читання з файлу
file_name = 'text_files/learning_python.txt'

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
    edit_line = line.replace('Python','Java').rstrip()
    print(edit_line)

print('\t')


print('\t')

def get_user_name():
    """Get user_name"""
    user_name = input('Enter your name: ')
    if not user_name:
        user_name = get_user_name()
    print(f"Hello {user_name}")
    return user_name

def write_user_info(user, ref='text_files/guest_book.txt'):
    """Write user info"""
    with open(ref, 'a', encoding="utf8") as user_object:
        user_object.write(f"Added info about user: {user} \n")
        print('Record was added!')

new_user = get_user_name()
write_user_info(new_user)

print('\t')

def get_sum_numbers():
    """Return sum"""
    point_break = True
    while point_break:
        num_1 = input('Enter num 1: ')
        num_2 = input('Enter num 2: ')
        try:
            sum_num = int(num_1) + int(num_2)
            point_break = False
        except ValueError:
            print('Value error!')
        else:
            print(f"sum = {sum_num}")

get_sum_numbers()

def update_file(file_ref, file_text=''):
    """Додавання у файл нової інформації"""
    with open(file_ref, 'w', encoding="utf8") as file_object:
        if file_text != '':
            file_object.write(file_text+ '\n')
        else:
            print('Enter text!')

update_file('text_files/cats.txt', 'cat Jonny')
update_file('text_files/cats.txt', 'cat Jessi')
update_file('text_files/cats.txt', 'cat Joie')

update_file('text_files/dogs.txt', 'dog Jeisy')
update_file('text_files/dogs.txt', 'dog Jeck')
update_file('text_files/dogs.txt', 'dog Joster')

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, I can't find that file.")

def get_favorite_number(user_name):
    """Get favorite user number"""
    # user_info = {user_name: user_numb,}
    try:
        with open('text_files/favorite_number.json', encoding="utf8") as file:
            user_info = json.load(file)
    except FileNotFoundError:
        return 0
    else:
        return user_info[user_name]

def get_username():
    """Prompt for a new user number."""
    user_name = input("What is your name? ")
    return user_name

number = get_favorite_number(get_username())

print(number)

try:
    print(f"I know your favorite number! It's {number}.")
except ValueError:
    print('Record was nor founded')
