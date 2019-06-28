import numpy as np
import matplotlib.pyplot as plt

data = 2 * np.random.rand(10000, 2) - 1
x = data[:, 0]
y = data[:, 1]
idx = x ** 2 + y ** 2 < 1
hole = x ** 2 + y ** 2 < 0.25
idx = np.logical_and(idx, ~hole)
plt.plot(x[idx], y[idx], 'go', markersize=1)
plt.show()

# x = np.array([1, 2, 3, 4])
# y = [True, False, True, True]
# print(x[y])  # 将打印出[1,3,4]
