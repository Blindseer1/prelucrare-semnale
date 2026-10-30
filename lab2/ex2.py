import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import sounddevice as sd

# Ex 2 si 3

f = 400
N = 1600
fs = 80000
a=1

n = np.arange(N)
t = n / fs

x = a*np.sin(2 * np.pi * f * t + np.pi/4)
y = a*np.sin(2 * np.pi * f * t + np.pi/2)
p = a*np.sin(2 * np.pi * f * t + np.pi)
m = a*np.sin(2 * np.pi * f * t + 3*np.pi/4)

fig, axs = plt.subplots(5)


def findY(x,z,snr):
    return np.sqrt(np.linalg.norm(x)**2 / (np.linalg.norm(z)**2 * snr))


z=np.random.normal(size=N)


axs[0].plot(t,x, color = 'green')
axs[0].plot(t,y, color = 'red')
axs[0].plot(t,p, color = 'cyan')
axs[0].plot(t,m, color = 'pink')
axs[1].plot(t,x+findY(x,z,0.1)*z, color = 'olivedrab')
axs[2].plot(t,y+findY(x,z,1)*z, color = 'chocolate')
axs[3].plot(t,p+findY(x,z,10)*z, color = 'mediumorchid')
axs[4].plot(t,m+findY(x,z,100)*z, color = 'dodgerblue')

plt.show()

rate = 10
sd.play(x,fs)
scipy.io.wavfile.write('song.wav', rate, x)
scipy.io.wavfile.read('./song.wav')

