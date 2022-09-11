import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания
rw = RandomWalk(1000)
rw.fill_walk()

# Нанесение точек на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()

ax.set_title("Random Walk", fontsize=18)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)

ax.scatter(rw.x_values, rw.y_values, s=25, c=rw.y_values, cmap=plt.cm.autumn)

plt.show()