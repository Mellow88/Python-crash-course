"Unit_3 Знайомство зі списками"

bicycles = ['Pride', 'Trek', 'Cannondale', 'Specialed']

print(bicycles)

# Додавання нового елементу списку
bicycles.append('Ducati')

print(bicycles)

# Додавання нового елементу списку на визначене місце
bicycles.insert(0, 'Suzuki')

print(bicycles)

#  Вилучення елемента у списку
del bicycles[0]
bicycles.pop(-1)

print(bicycles)

message = f"My first bicycle was a {bicycles[0].title()}"

print(message)

# Сортування списку
bicycles.sort()
print(bicycles)

bicycles.sort(reverse = True)
print(bicycles)

# Відображення відсортованого списку
print(sorted(bicycles))
print(bicycles.reverse())
