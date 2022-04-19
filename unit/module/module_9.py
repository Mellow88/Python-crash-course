"""Збереження класів у модулях"""

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
