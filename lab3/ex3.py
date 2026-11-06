import numpy as np
import matplotlib.pyplot as plt

N = 1000
n = np.arange(N)
f = [10, 40, 90]
x = 1 * np.sin(2 * np.pi * f[0] * n / N) + 0.5 * np.sin(2 * np.pi * f[1] * n / N) + 0.8 * np.sin(2 * np.pi * f[2] * n / N)

w = np.arange(0, 2 * max(f) + 1)
F = np.exp(-2j * np.pi * w.reshape(-1, 1) * n.reshape(1, -1) / N)
X = np.abs(F @ x)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(n / N, x)
plt.xlabel("t [s]")
plt.ylabel("x")
plt.subplot(1, 2, 2)
plt.stem(w, X)
plt.xlabel("ω [Hz]")
plt.ylabel("|X(ω)|")
plt.tight_layout()
plt.show()
