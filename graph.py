#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt


x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.391, 0.042, 0.007])

plt.title("Graph Of Screen Analysis Experiment Using Set of Sieve A")
plt.xlabel("mass fraction")
plt.ylabel("particle size")



plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.grid()


#Two  lines to make our compiler able to draw:

#######

#plot 2:

x = np.array([2.000, 0.589, 0.053, 0.063])
y = np.array([0.476, 0.867, 0.909, 0.916])

plt.xlabel("cumulative fraction")
plt.ylabel("particle size")
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.grid()
plt.show()

#Two  lines to make our compiler able to draw:

plt.savefig('screen_analysis.pdf')
