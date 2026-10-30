import numpy as np
import matplotlib.pyplot as plt

alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)
s = np.sin(alpha)
taylor = alpha

pade = (alpha - 7 * alpha**3 / 60) / (1 + alpha**2 / 20)

err_taylor = np.abs(s - taylor)
err_pade = np.abs(s - pade)

fig, axs = plt.subplots(3)

axs[0].plot(alpha, s )
axs[0].plot(alpha, taylor)
axs[0].plot(alpha, pade)

axs[1].plot(alpha, err_taylor)
axs[1].plot(alpha, err_pade)

axs[2].semilogy(alpha, err_taylor)
axs[2].semilogy(alpha, err_pade)

plt.show()
