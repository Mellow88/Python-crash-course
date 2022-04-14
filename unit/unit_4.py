"Unit_4 Робота зі списками"

magicains = ['alice', 'david', 'carolina']

for mag in magicains:
    print(f"{mag.title()}, that was a great trick!")
    print(f"I can not wait see your next trick, {mag.title()}.\n")

print("Thank you, every one!")

# Числові списки

for value in range(1, 5):
    print(value)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Генераторні списки

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Розбиття списку  на слайси

players = ['cgarles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[:-3])
print(players[-3:])

# Кортежі

dimensions = (200, 50)
print(dimensions)
