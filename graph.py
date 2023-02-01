import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)

ax.grid(linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
plt.savefig('screen.pdf')
