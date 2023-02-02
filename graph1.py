import numpy as np
import matplotlib.pyplot as plt

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10),
                                              gridspec_kw={'hspace': 0.4, 'wspace': 0.4})

x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.391, 0.042, 0.007])

ax1.plot(x, y)
ax1.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve A")
ax1.set_xlabel("Particle Size")
ax1.set_ylabel("Mass Fraction")
ax1.grid()


x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.867, 0.909, 0.916])

ax2.plot(x,y)
ax2.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve B")
ax2.set_xlabel("Particle Size")
ax2.set_ylabel("Cumulative Fraction")
ax2.grid()
x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.391, 0.042, 0.007])

ax3.plot(x, y)
ax3.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve C")
ax3.set_xlabel("Particle Size")
ax3.set_ylabel("Mass Fraction")
ax3.grid()
x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.867, 0.909, 0.916])

ax4.plot(x,y)
ax4.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve D")
ax4.set_xlabel("Particle Size")
ax4.set_ylabel("Cumulative Fraction")
ax4.grid()
fig.tight_layout(pad=5.0)
plt.show()
plt.savefig("analysis.pdf")
