import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 3, 50)
y = x ** x
plt.plot(x, y, 'r', linewidth=2, label='y=x**x')
plt.legend(loc='lower right')
plt.show()
