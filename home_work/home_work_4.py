"""HW_4"""

for value in range(1, 21, 2):
    print(value)

numbers = [value for value in range(1, 1_000_001)]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers_3 = []
for value in range(3, 30):
    if value % 3 == 0:
        numbers_3.append(value)
print(numbers_3)

list_pizzas = ['red', 'blue', 'green', 'white', 'yellow']
double_pizzas = list_pizzas[:]

list_pizzas.append('orange')
double_pizzas.append('blue')

print(list_pizzas)
print(double_pizzas)
print('\n')

menu = ('apple', 'tomatos', 'pineapple', 'bear', 'spagetti')
print(f"Old menu: {menu}")

menu = ('nut', 'tomatos', 'pineapple', 'bear', 'pasta')
print(f"New menu: {menu}")
