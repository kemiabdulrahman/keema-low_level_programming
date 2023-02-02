import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2,ax3, ax4) = plt.subplots(4, 1, figsize=(10,22))
                                            # gridspec_kw={'hspace': 0.4, 'wspace': 0.4})

x = np.array([10,28,53,63,"PAN"])
y = np.array([0.476, 0.391, 0.042, 0.007,0.073])

ax1.plot(x, y)
ax1.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve A")
ax1.set_xlabel("Particle Size")
ax1.set_ylabel("Mass Fraction")
ax1.grid()


x = np.array([10,28,53,63,"PAN"])
y = np.array([0.476,0.867,0.909,0.916,0.989])
ax2.plot(x,y)
ax2.set_xlabel("Particle Size")
ax2.set_ylabel("Cumulative Fraction")
ax2.grid()

x = np.array([10,14,18,30,50,70,"PAN"])
y = np.array([0.5650,0.1200,0.1210,0.0790,0.0390,0.0427,0.0143])

ax3.plot(x, y)
ax3.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve B")
ax3.set_xlabel("Particle Size")
ax3.set_ylabel("Mass Fraction")
ax3.grid()
x = np.array([10,14,18,30,50,70,"PAN"])
y = np.array([0.565, 0.685, 0.806,0.885 ,0.924,0.967,0.981])

ax4.plot(x,y)
ax4.set_xlabel("Particle Size")
ax4.set_ylabel("Cumulative Fraction")
ax4.grid()
fig.tight_layout(pad=5.0)
plt.show()
plt.savefig("analysis.pdf")
