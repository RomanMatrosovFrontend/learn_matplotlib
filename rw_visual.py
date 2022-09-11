import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    # Построение случайного блуждания
    rw = RandomWalk(1000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()

    ax.set_title('Random Walk', fontsize=18)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=25, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')

    ax.scatter(0, 0, s=50, c='green', edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=50, c='red', edgecolors='none')

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input('Повторить? (y/n)\n')
    if keep_running == 'n':
        break