"""Класи"""

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
