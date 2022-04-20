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
