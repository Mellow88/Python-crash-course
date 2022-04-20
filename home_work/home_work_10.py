"""HW_10"""

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
