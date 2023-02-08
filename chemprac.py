import numpy as np
import matplotlib.pyplot as plt

x1 = [0, 300, 600, 900, 1200, 1500, 1800, 2100, 72000]
y1 = [24.00, 20.80, 17.90, 16.20, 14.00, 11.80, 9.60, 6.60, 1.70]

x2 = np.random.randint(0, 72000, 9)
y2 = np.random.randint(0, 30, 9)

x3 = np.random.randint(0, 72000, 9)
y3 = np.random.randint(0, 30, 9)

x4 = np.random.randint(0, 72000, 9)
y4 = np.random.randint(0, 30, 9)

fig, axs = plt.subplots(4, 1, figsize=(8, 12))
axs[0].plot(x1, y1, label='Graph 1')
axs[0].set_title("Graph 1")

axs[1].plot(x2, y2, label='Graph 2')
axs[1].set_title("Graph 2")

axs[2].plot(x3, y3, label='Graph 3')
axs[2].set_title("Graph 3")

axs[3].plot(x4, y4, label='Graph 4')
axs[3].set_title("Graph 4")

fig.suptitle("Plot of height of interface against time")
plt.tight_layout()
plt.show()

