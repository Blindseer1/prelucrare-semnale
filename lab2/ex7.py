import numpy as np
import matplotlib.pyplot as plt

f = 100
fs = 1000
N = 200
a = 1

n = np.arange(N)
t = n / fs
x = a * np.sin(2 * np.pi * f * t)

x1 = x[::4]
t1 = t[::4]

x2 = x[1::4]
t2 = t[1::4]

fig, axs = plt.subplots(3)

axs[0].stem(t, x)
axs[1].stem(t1, x1)
axs[2].stem(t2, x2)

plt.show()

# Semnalul decimat are mai putine esantioane deci sinusoida este desenata cu 
# mai putine puncte
#
# Informatia ramane la fel, doar faza de incepute se schimba
