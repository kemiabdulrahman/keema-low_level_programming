import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([2.000, 0.589, 0.053, 0.063]) 
y = np.array([0.476, 0.391, 0.042, 0.007]) 

plt.title("Graph Of Screen Analysis Experiment Using Set of Sieve A") 
plt.xlabel("Particle Size") 
plt.ylabel("Mass Fraction") 

plt.subplot(2, 1, 1, gridspec_kw={'height_ratios': [3, 1]}) 
plt.plot(x, y) 
plt.show 

# Two lines to make our compiler able to draw: 

####### 

# plot 2: 

x = np.array([2.000, 0.589, 0.053, 0.063]) 
y = np.array([0.476, 0.867, 0.909, 0.916]) 

plt.xlabel("Particle Size") 
plt.ylabel("Cumulative Fraction") 
plt.subplot(2, 1, 2, gridspec_kw={'height_ratios': [1, 3]}) 
plt.plot(x, y) 

plt.grid() 
plt.show() 

plt.savefig('screen_analysis.pdf')

