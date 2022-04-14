"Оператор IF"

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

CAR_EX = 'suzuki' in cars
print(CAR_EX)

users = ['olha', 'ihor', 'natali']

AGE = 19

if AGE >= 18:
    print('You are old enough to vote')
else:
    print('Sorry, you are too young to vote')

AGE = 12

if AGE < 4:
    PRICE = 0
elif AGE < 18:
    PRICE = 25
else:
    PRICE = 40

print(f"Your admission cost is {PRICE}$")

request_topings = []
request_topings.append('mushrooms')
request_topings.append('green peppers')
request_topings.append('extra cheese')

if request_topings:
    for req_top in request_topings:
        print(req_top)
else:
    print('Are you sure you want pizza?')
