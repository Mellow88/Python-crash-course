"""Unit_2 Змінні та найпростіші типи данних"""

# import this

# NOTE: Формативання рядка
first_name = 'Ihor'
last_name = 'Sereda'
full_name = f"{first_name} {last_name}"

message = f"Hello, {full_name}!"

print(message)

# NOTE: Пробільні символи та табуляція
print("Languages:\n\tPython\n\t1C")

# NOTE: Прибрати пробыли з рядка
favorite_food = "icecream "
favorite_food.lstrip()
favorite_food.rstrip()
favorite_food.strip()

print(favorite_food)

# NOTE: Робота з числами

CONST_NUM = 5_000

print(CONST_NUM)
print(3 * 0.1)
