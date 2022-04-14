"""HW_7"""

car = input('What car you want rent? ')
message = f"Let me see if I can find {car} model for you"

print(message)

place_count = input('How many places need for you? ')
place_count = int(place_count)

if place_count > 8:
    print("We dont have any places for you")
else:
    print("You places are free")

while True:
    new_topping = input('Enter new topping for you pizza: ')
    message = 'Your pizza has prepared'
    if new_topping != 'quit':
        print(message)
    else:
        break

category_ticket_price = 0

while True:
    age = input('How old are you?')

    if int(age) > 3:
        price = 10
    elif int(age) > 12:
        price = 15
    else:
        price = 0
    message = f"\tTicket price: {price}"
    print(message)

sandwich_orders = ['chiken', 'pastrami', 'cheese', 'pastrami',
                   'potato', 'tuna', 'pastrami']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich} sandwich")

print(sandwich_orders)
print(finished_sandwiches)
