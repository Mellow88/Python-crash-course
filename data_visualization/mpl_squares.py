"""Mpl_squares"""

import matplotlib.pyplot as plt

# NOTE: Дані для діаграми
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# NOTE: Викликаємо функцію 'subplots()' - піддіаграми
# NOTE: Дозволяє генерувати  більше однієї діаграми на рисунку

# NOTE: Змінна fig - весь рисунок
# NOTE: Змінна ax - діаграма
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# NOTE: Побудова діаграми
# ax.plot(values, squares, linewidth=3)

# NOTE: Задати назву графіка та кожної з осей
ax.set_title("Squares numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# NOTE: Встановлення мін та макс значень по осям координат
ax.axis([0, 1100, 0, 1100000])

ax.ticklabel_format(useOffset=False, style='plain')

# NOTE: Задати розмыр шрифту кожної з осей
ax.tick_params(axis='both', labelsize=8)

# NOTE: відкриття діаграми до перегляду
plt.show()
