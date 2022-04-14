"""Функції"""


def greet_user(username):
    """Показати просте вітання"""
    print(f"Hello, {username.title()} !")


greet_user('jesee')


# NOTE: Ключові аргументи у функції
def describe_pet(pet_name, animal_type='dog'):
    """Показати інформацію про домашнього улюбленця"""
    print(f"My animal's {animal_type}, name is {pet_name}")


describe_pet(pet_name='harry')

# NOTE: Необовязкові аргументи у функції
def get_formatted_name(first_name, last_name, middle_name=''):
    """Повернення відформатованого імені"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimmi', 'hendrix', 'lee')
print(musician)

def build_person(firs_name, last_name, age=None):
    """Повернення словника з інформацією про людину"""
    person = {'firs_name': firs_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimmi', 'hendrix', 44)
print(musician)

# NOTE: Передавання списку
def greet_users(names):
    """Виведення повідомленння для користувача"""
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

username = ['ihor', 'nataly', 'olha']
greet_users(username)

models_uncomleted = ['model_1', 'model_2', 'model_3']
models_completed = []

def print_models(models_uncomleted, models_completed):
    """Друк поточного креслення
       Перенесення моделы після друку
    """
    while models_uncomleted:
        current_model = models_uncomleted.pop()
        print(f"Printing model: {current_model}")
        models_completed.append(current_model)

def show_models(models):
    """sss"""
    for model in models:
        print(f"Completed model: {model}")

print_models(models_uncomleted, models_completed)
show_models(models_completed)
