import numpy as np
import matplotlib.pyplot as plt

#
# f = 400
# N = 1600
# fs = 80000
#
# n = np.arange(N)
# t = n/fs
# x = np.sin(2*np.pi*f*t)
#
# plt.figure()
# plt.plot(t,x)
# plt.show()


# f = 800
# T = 3
# fs = 1 / T
# N = 100
#
# n = np.arange(N)
# t = n / fs
# x = np.sin(2 * np.pi * f * t)
#
# plt.figure()
# plt.plot(t, x)
# plt.show()


# f= 240
# def x(t):
#     return 2*(f*t-np.floor(f*t)) - 1
#
# N=1000
# t=np.linspace(0,1,N)
# plt.figure()
# plt.plot(t, x(t))
# plt.show()




# f = 300
# def x(t):
#     return np.sign(np.sin(2 * np.pi * t * f)) - 1
# N = 1000
# t = np.linspace(0, 0.2, N)
# plt.figure()
# plt.plot(t, x(t))
# plt.show()

# n=np.random.rand(128,128)
# plt.imshow(n)
# plt.show()


n=np.ones((128,128))
n[100:150]= 0
plt.imshow(n)
plt.show()


# Ex3 
# a. T = 1/2000 = 0.5 ms 
# b.N = 2000 * 3600 = 72 * 10^5
# Nr biti=  N*4 = 288 * 10^5
# Nr bytes = Nr biti/8 = 35*10^5




