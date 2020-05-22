import numpy as np
import matplotlib.pyplot as plt

x = np.arange(14)
y = np.cos(5 * x)

plt.plot(x, y + 2, 'blue', linestyle="-", label="niebieski")

plt.plot(x, y + 1, 'red', linestyle=":", label="czerwony")

plt.plot(x, y, 'green', linestyle="--", label="zielony")

plt.legend(title='Legenda:')
plt.show()