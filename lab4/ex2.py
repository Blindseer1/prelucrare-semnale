import numpy as np
import matplotlib.pyplot as plt

f = 7
fs = 10

t = np.linspace(0, 1, 1000)
n = np.arange(0, 1, 1 / fs)

f1 = f - fs
f2 = f + fs

plt.plot(t, np.sin(2 * np.pi * f * t), label=f"{f} Hz")
plt.plot(t, np.sin(2 * np.pi * f1 * t), label=f"{f1} Hz")
plt.plot(t, np.sin(2 * np.pi * f2 * t), label=f"{f2} Hz")
plt.stem(n, np.sin(2 * np.pi * f * n), linefmt="k-", markerfmt="ko", basefmt=" ")
plt.xlabel("t (s)")
plt.legend()
plt.show()
