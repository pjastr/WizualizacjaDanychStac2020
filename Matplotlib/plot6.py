import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 10)
y = x ^ 2
z = x ^ 3
t = x ^ 4
# Labeling the Axes and Title
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(x, y)

# Annotate
plt.annotate(xy=[2, 1], s='Second Entry')
plt.annotate(xy=[4, 6], s='Third Entry')
# Adding Legends
plt.plot(x, z)
plt.plot(x, t)
plt.legend(['Race1', 'Race2', 'Race3'], loc=4)
plt.show()
