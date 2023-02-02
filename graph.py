import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.391, 0.042, 0.007])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

ax1.plot(x, y)
ax1.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve A")
ax1.set_ylabel("Mass Fraction")
ax1.grid()


x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.867, 0.909, 0.916])

ax2.plot(x,y)
ax2.set_xlabel("Particle Size")
ax2.set_ylabel("Cumulative Fraction")
ax2.grid()


fig.tight_layout()
plt.savefig('screen a.pdf')
plt.show()

