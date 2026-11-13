import time
import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    n = np.arange(len(x))
    return np.array([np.dot(x, np.exp(-2j * np.pi * k * n / len(x))) for k in n])


def fft(x):
    n = len(x)
    if n == 1:
        return x
    e = fft(x[0::2])
    o = fft(x[1::2])
    t = np.exp(-2j * np.pi * np.arange(n // 2) / n) * o
    return np.concatenate([e + t, e - t])


sizes = [128, 256, 512, 1024, 2048, 4096, 8192]
dftTimes = []
fftTimes = []
numpyTimes = []

for n in sizes:
    x = np.random.rand(n)

    start = time.time()
    dft(x)
    dftTimes.append(time.time() - start)

    start = time.time()
    fft(x)
    fftTimes.append(time.time() - start)

    start = time.time()
    np.fft.fft(x)
    numpyTimes.append(time.time() - start)

plt.plot(sizes, dftTimes, label="DFT")
plt.plot(sizes, fftTimes, label="FFT")
plt.plot(sizes, numpyTimes, label="numpy")
plt.yscale("log")
plt.legend()
plt.show()
