import numpy as np
import matplotlib.pyplot as plt

fs = 80000
N = 20
a = 1

n = np.arange(N)
t = n / fs

x1 = a * np.sin(2 * np.pi * (fs / 2) * t)
x2 = a * np.sin(2 * np.pi * (fs / 4) * t)
x3 = a * np.sin(2 * np.pi * 0 * t)

fig, axs = plt.subplots(3)

axs[0].stem(t, x1)
axs[1].stem(t, x2)
axs[2].stem(t, x3)

plt.show()
