"""Класи"""

from random import choice
from module import module_9

players = ['Martina', 'Nataly', 'Jonny']
random_player = choice(players)

print(random_player)

# NOTE: Створення та використанння класу
class Dog:
    """Проста спроба змоделювати собаку"""

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def sit(self):
        """Виконання команди 'Сидіти'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Виконання команди 'Лежати'."""
        print(f"{self.name} rollled over!")

# NOTE: Створення екземпляру класу
my_dog = Dog('Jessi', 7)
print(f"{my_dog.name.title()} is my dogs")
print(f"My dog is {my_dog.age} years old")


my_dog.roll_over()
my_dog.sit()

class Car:
    """Моделювання класу 'Car'"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів що описують клас"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def get_name(self):
        """Return format car name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometr(self):
        """Read car odometr"""
        print(f"This car has {self.odometr} miles on it.")

    def update_odometr(self, miles):
        """Задання значення одометра"""
        if miles >= self.odometr:
            self.odometr = miles
        else:
            print('Can not roll back an odometr!')

    def increment_odometr(self, miles):
        """Додати задане значення до показника одометру"""
        if miles < 0:
            print('Can not roll back an odometr!')
        else:
            self.odometr += miles

    def fill_gas_tank(self):
        """Виведення повідомлення про заповнення баку"""
        print("Gas tank is full")


new_car = Car('audi', 'a4', 2019)
new_car.get_name()

# NOTE: Зміна атрибута класу та його безпосереднє читання
new_car.odometr = 34
new_car.update_odometr(56)
new_car.increment_odometr(10)
new_car.read_odometr()

# NOTE: Успадкування класів
class ElectricCar(Car):
    """Моделювання класу ElectricCar."""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів що описують клас
           Тоді ініціалізація атрибутів електрокара
        """
        super().__init__(make, model, year)
        self.battery_size = Battery()

    # def describe_barttery(self):
    #     """Виведення повідомлення про розмір акумулятора"""
    #     print(f"This car has a {self.battery_size}-kWh battery")

    # NOTE: Перевизначення методів батьківського класу
    def fill_gas_tank(self):
        """Електрокари не мають баків"""
        print('This car does not need a gas tank')

class Battery:
    """docstring for Battery."""

    def __init__(self, battery_size=75):
        """Ініціалізація атрибутів акумулятора"""
        self.battery_size = battery_size

    def describe_barttery(self):
        """Виведення повідомлення про розмір акумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """
        Виведення повідомлення про відстань,
        яку може проїхати авто відповідно
        до ємкості акумулятора
        """
        # car_range = 0
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315

        print(f"This car can go about {car_range} miles on a full charge")

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print("The battery is already upgraded.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.odometr = 200
print(my_tesla.get_name())
my_tesla.battery_size.describe_barttery()
my_tesla.battery_size.get_range()
my_tesla.battery_size.upgrade_battery()
my_tesla.battery_size.get_range()

new_car.fill_gas_tank()
my_tesla.fill_gas_tank()

# NOTE: Імпортування класів з окремого модуля
my_car = module_9.Car('audi', 'a4', 2010)
print(my_car.get_name())
