import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

f = 3
t = np.linspace(0, 1, 500)
x = np.sin(2 * np.pi * f * t)
c = np.abs(x)
w = [1, 25, f, 6]

z = x * np.exp(-2j * np.pi * f * t)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.scatter(t, x, c=c, s=3, cmap="plasma")
plt.subplot(1, 2, 2)
plt.scatter(z.real, z.imag, c=c, s=3, cmap="plasma")
plt.axis("equal")

plt.figure(figsize=(16, 4))
for i in range(4):
    zi = x * np.exp(-2j * np.pi * w[i] * t)
    plt.subplot(1, 4, i + 1)
    plt.scatter(zi.real, zi.imag, c=c, s=3, cmap="plasma")
    plt.title(f"ω = {w[i]}")
    plt.axis("equal")

fig1, ax1 = plt.subplots(1, 2, figsize=(10, 4))
ax1[0].set_xlim(0, 1)
ax1[0].set_ylim(-1.1, 1.1)
ax1[1].set_xlim(-1.1, 1.1)
ax1[1].set_ylim(-1.1, 1.1)
ax1[1].set_aspect("equal")
s0 = ax1[0].scatter(t[:1], x[:1], c=c[:1], s=3, cmap="plasma", vmin=0, vmax=1)
s1 = ax1[1].scatter(z.real[:1], z.imag[:1], c=c[:1], s=3, cmap="plasma", vmin=0, vmax=1)
d0 = ax1[0].plot([], [], "ko")[0]
d1 = ax1[1].plot([], [], "ko")[0]

def update1(n):
    s0.set_offsets(np.c_[t[:n + 1], x[:n + 1]])
    s0.set_array(c[:n + 1])
    s1.set_offsets(np.c_[z.real[:n + 1], z.imag[:n + 1]])
    s1.set_array(c[:n + 1])
    d0.set_data([t[n]], [x[n]])
    d1.set_data([z.real[n]], [z.imag[n]])

anim1 = FuncAnimation(fig1, update1, frames=len(t), interval=20)

fig2, ax2 = plt.subplots(1, 4, figsize=(16, 4))
zs = []
scs = []
dots = []
for i in range(4):
    zs.append(x * np.exp(-2j * np.pi * w[i] * t))
    ax2[i].set_xlim(-1.1, 1.1)
    ax2[i].set_ylim(-1.1, 1.1)
    ax2[i].set_aspect("equal")
    ax2[i].set_title(f"ω = {w[i]}")
    scs.append(ax2[i].scatter(zs[i].real[:1], zs[i].imag[:1], c=c[:1], s=3, cmap="plasma", vmin=0, vmax=1))
    dots.append(ax2[i].plot([], [], "ko")[0])

def update2(n):
    for i in range(4):
        scs[i].set_offsets(np.c_[zs[i].real[:n + 1], zs[i].imag[:n + 1]])
        scs[i].set_array(c[:n + 1])
        dots[i].set_data([zs[i].real[n]], [zs[i].imag[n]])

anim2 = FuncAnimation(fig2, update2, frames=len(t), interval=20)

plt.show()
