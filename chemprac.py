import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

fig, (ax1, ax2,ax3, ax4) = plt.subplots(4, 1, figsize=(10,22))

x = np.array([10,28,53,63,45])
y = np.array([0.476, 0.391, 0.042, 0.007,0.073])

cubic_interpolation_model = interp1d(x, y, kind = "cubic")

X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interpolation_model(X_)

ax1.plot(X_, Y_)
ax1.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve A")
ax1.set_xlabel("Particle Size")
ax1.set_ylabel("Mass Fraction")
ax1.grid()


x = np.array([10,28,53,63,67])
y = np.array([0.476,0.867,0.909,0.916,0.989])

cubic_interpolation_model = interp1d(x, y, kind = "cubic")

X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interpolation_model(X_)

ax2.plot(X_,Y_)
ax2.set_xlabel("Particle Size")
ax2.set_ylabel("Cumulative Fraction")
ax2.grid()

x = np.array([10,14,18,30,50,70,56])
y = np.array([0.5650,0.1200,0.1210,0.0790,0.0390,0.0427,0.0143])

cubic_interpolation_model = interp1d(x, y, kind = "cubic")

X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interpolation_model(X_)

ax3.plot(X_, Y_)
ax3.set_title("Graph Of Screen Analysis Experiment Using Set of Sieve B")
ax3.set_xlabel("Particle Size")
ax3.set_ylabel("Mass Fraction")
ax3.grid()

x = np.array([10,14,18,30,50,70,56])
y = np.array([0.565, 0.685, 0.806,0.885 ,0.924,0.967,0.981])

cubic_interpolation_model = interp1d(x, y, kind = "cubic")

X_=np.linspace(x.min(), x.max(), 500)
Y_=cubic_interpolation_model(X_)

ax4.plot(X_,Y_)
ax4.set_xlabel("hello")
ax4.set_ylabel("hi")
ax4.grid()

