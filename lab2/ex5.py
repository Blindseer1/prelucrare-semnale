import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

f1 = 400
f2 = 900
fs = 44100
N = 44100
a = 1

n = np.arange(N)
t = n / fs
x = a * np.sin(2 * np.pi * f1 * t)
s = a * np.sin(2 * np.pi * f2 * t)

xs = np.concatenate((x, s))
t_total = np.arange(2 * N) / fs

plt.plot(t_total,xs)
plt.xlabel("Timp [s]")
plt.ylabel("Amplitudine")
plt.show()

sd.play(xs, fs)
sd.wait()

# Obs: Al doilea are un pitch mai ridicat
