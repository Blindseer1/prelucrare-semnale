import numpy as np
import matplotlib.pyplot as plt

f = 7
fs = 40
f1 = f - 10
f2 = f + 10

t = np.linspace(0, 1, 1000)
n = np.arange(0, 1, 1/fs)

plt.plot(t, np.sin(2*np.pi*f*t), label=f'{f} Hz')
plt.plot(t, np.sin(2*np.pi*f1*t), label=f'{f1} Hz')
plt.plot(t, np.sin(2*np.pi*f2*t), label=f'{f2} Hz')
plt.stem(n, np.sin(2*np.pi*f*n), linefmt='k-', markerfmt='ko', basefmt=' ')
plt.stem(n, np.sin(2*np.pi*f1*n), linefmt='r-', markerfmt='ro', basefmt=' ')
plt.stem(n, np.sin(2*np.pi*f2*n), linefmt='g-', markerfmt='go', basefmt=' ')
plt.xlabel('t (s)')
plt.legend()
plt.show()
