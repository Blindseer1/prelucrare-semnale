import numpy as np
import matplotlib.pyplot as plt
import math

N = 8
m = np.arange(N).reshape(N, 1)
k = np.arange(N).reshape(1, N)
F = math.e**(
    -2j * np.pi * m * k/ N
)


fig, axs = plt.subplots(N, 1, figsize=(8, 14), sharex=True)
for i in range(N):
    axs[i].plot(F[i].real, color="firebrick", label="real")
    axs[i].plot(F[i].imag, color="darkmagenta", label="imag")
    axs[i].set_ylabel(f"row {i}")
plt.show()


print(F)
FHF = F.conj().T @ F
print("allclose:", np.allclose(FHF, N * np.eye(N)))
