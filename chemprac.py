import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2,ax3, ax4) = plt.subplots(4, 1, figsize=(10,22))
                                            # gridspec_kw={'hspace': 0.4, 'wspace': 0.4})

x = np.array([5.0, 5.5,6.0,6.5,8.0,8.5,9.0,9.5,10.0])
y = np.array([1.12,1.09,1.06,1.29,1.49,1.57,1.63,1.65,1.70])

ax1.plot(x, y)
ax1.set_xlabel("volume of naoh acetic acid")
ax1.set_ylabel("conductivity")
ax1.grid()


x = np.array([1.00,1.20,1.60,1.80,2.00,2.20,2.40,2.69])
y = np.array([1.08,0.93,0.73,0.69,0.73,0.79,0.81,0.83])
ax2.plot(x,y)
ax2.set_xlabel("volume of naoh hcl")
ax2.set_ylabel("Conductivity")
ax2.grid()

x = np.array([400,420,440,460,480,500,520,540,560,580,600])
y = np.array([0.084,0.070,0.065,0.065,0.073,0.091,0.110,0.105,0.072,0.044,0.025])

ax3.plot(x, y)
ax3.set_xlabel("wavelength")
ax3.set_ylabel("absorbance")
ax3.grid()
x = np.array([0.0001,0.0002,0.0003,0.0004,0.0005,0.0006])
y = np.array([0.016,0.057,0.092,0.132,0.152,0.182])

ax4.plot(x,y)
ax4.set_xlabel("concentration")
ax4.set_ylabel("absorbance")
ax4.grid()
fig.tight_layout(pad=5.0)
plt.show()
plt.savefig("chemprac.pdf")
