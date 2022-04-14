"""Збереження функцій у модулях"""

def make_pizza(size, *args):
    """Описати піцу яку збираємсь приготувати"""
    print(f"\nMaking a pizza {size}-inch pizza with folowing toppings:")
    for topping in args:
        print('\t' + topping)
