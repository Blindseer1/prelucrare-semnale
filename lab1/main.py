import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.cos(520*np.pi*t + np.pi/3)

def y(t):
    return np.cos(280*np.pi*t - np.pi/3)

def z(t):
    return np.cos(120*np.pi*t + np.pi/3)


n=3
fig, axs = plt.subplots(n)


fs = 200
T = 1/200


tn = np.arange(0,0.03,T)
n= np.arange(len(tn))
xn = x(tn)
yn = y(tn)
zn = z(tn)


axs[0].stem(n,xn) 
axs[1].stem(n,yn) 
axs[2].stem(n,zn)



# t= np.linspace(0,0.03,100)
# axs[0].plot(t,x(t))
# axs[0].stem(t,x(t))
# axs[1].plot(t,y(t))
# axs[1].stem(t,y(t))
# axs[2].plot(t,z(t))
# axs[2].stem(t,z(t))
plt.show()

