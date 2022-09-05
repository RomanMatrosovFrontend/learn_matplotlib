import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of value", fontsize=12)

# Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=10)

plt.show()