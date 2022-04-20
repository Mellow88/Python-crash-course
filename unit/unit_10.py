"""Файли та винятки"""


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
