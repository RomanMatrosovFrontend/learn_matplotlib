import matplotlib.pyplot as plt

x_values = range(50)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.autumn)

plt.show()