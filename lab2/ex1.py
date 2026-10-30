import numpy as np
import matplotlib.pyplot as plt


f = 400
N = 1600
fs = 80000
a=1

n = np.arange(N)
t = n / fs
x = a*np.sin(2 * np.pi * f * t)

n = np.arange(N)
t = n / fs
y = a*np.cos(2 * np.pi * f * t- np.pi/2)

fig, axs = plt.subplots(2)

axs[0].plot(t,x, color = 'green')
axs[1].plot(t,y, color = 'red')


plt.show()
