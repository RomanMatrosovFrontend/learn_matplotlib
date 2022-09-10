import matplotlib.pyplot as plt

x_values = range(200)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=20, c=y_values, cmap=plt.cm.autumn)

# Назначение заголовка диаграммы и меток осей
ax.set_title("Square numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Square of value", fontsize=16)

ax.tick_params(axis="both", which="major", labelsize=12)

ax.axis([0, 400, 0, 40000])

# plt.show()
plt.savefig('scatter_squares.png', bbox_inches='tight')