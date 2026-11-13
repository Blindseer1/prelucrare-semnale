import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

fs, x = wavfile.read("./aeiou.wav")
if x.ndim > 1:
    x = x[:, 0]

N = len(x)
w = N // 100
h = w // 2

cols = []
for i in range(0, N - w + 1, h):
    cols.append(np.abs(np.fft.rfft(x[i : i + w])))

S = np.array(cols).T

plt.imshow(20 * np.log10(S + 1e-6), aspect="auto", origin="lower")
plt.xlabel("grup")
plt.ylabel("frecventa")
plt.colorbar()
plt.show()
