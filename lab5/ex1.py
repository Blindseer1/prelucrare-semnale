# a. Frecventa Fs este 1/3600( una pe ora)
# b. Un interval de 76 de ore
# c. Fs = 2* fmax; fmax = 1/7200
# d

import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("Train.csv", delimiter=",", skip_header=1, usecols=[2])
N = len(x)
Fs = 1 / 3600  # Hz, un esantion pe ora
print("N =", N, " Fs =", Fs, " f_max =", Fs / 2)

X = np.abs(np.fft.fft(x) / N)
f = np.fft.fftfreq(N, d=1 / Fs)
plt.figure()
plt.plot(f[: N // 2], X[: N // 2])
plt.xlabel("f [Hz]")
plt.ylabel("|X(f)|")

# (e)
print("componenta continua =", np.mean(x))
x2 = x - np.mean(x)
X = np.abs(np.fft.fft(x2) / N)
plt.figure()
plt.plot(f[: N // 2], X[: N // 2])
plt.xlabel("f [Hz]")
plt.ylabel("|X(f)|")

# (f)
Xp = X[: N // 2]
fp = f[: N // 2]
lista = []
for k in range(101, N // 2 - 1):
    if Xp[k] > Xp[k - 1] and Xp[k] > Xp[k + 1]:
        lista.append(k)
lista.sort(key=lambda k: Xp[k], reverse=True)
for k in lista[:4]:
    print("k =", k, " f =", fp[k], " perioada [h] =", 1 / fp[k] / 3600, " |X| =", Xp[k])

# (g)
# luni=48+168*k;k=6->1056
start = 1056
plt.figure()
plt.plot(x[start : start + 720])
plt.xlabel("ora")
plt.ylabel("nr. masini")

# (h)
# 1. se face media pe pozitia din saptamana (168 h);
#    cele 2 zile consecutive cu trafic minim sunt sambata si duminica
# 2. media pe ora din zi  da ora; minimul e noaptea
# 3. sarbatorile apar ca zile cu trafic mic in
#    mijlocul saptamanii si au data exacta
w = x[: N - N % 168].reshape(-1, 168).mean(axis=0)
print("media pe zile:", w.reshape(7, 24).mean(axis=1))

# (i)
fc = 4 / 86400
Y = np.fft.fft(x)
Y[np.abs(f) > fc] = 0
xf = np.real(np.fft.ifft(Y))
plt.figure()
plt.plot(x[start : start + 720], label="original")
plt.plot(xf[start : start + 720], label="filtrat")
plt.legend()

plt.show()
