import numpy as np
import matplotlib.pyplot as plt

f = 400
N = 1600
fs = 80000
a = 1

n = np.arange(N)
t = n / fs
x = a * np.sin(2 * np.pi * f * t)
s = 2 * (f * t - np.floor(f * t)) - 1

fig, axs = plt.subplots(3)

axs[0].plot(t, x, color="firebrick")
axs[1].plot(t, s, color="darkmagenta")
axs[2].plot(t, s+x, color="lightsteelblue")


plt.show()
