import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

density, iterator = 300, 200
radius = 1.5

x = np.linspace(-2.5, 1.5, 4 * density + 1)
y = np.linspace(-1.5, 1.5, 3 * density + 1)

A, B = np.meshgrid(x, y)
C = A + B * 1j

Z = np.zeros_like(C)
T = np.zeros(C.shape)

for k in range(iterator):
    M = abs(Z) < radius
    Z[M] = Z[M] ** 2 + C[M]
    T[M] = k + 1


plt.imshow(T, cmap=plt.cm.twilight_shifted)
plt.savefig("Mandelbrot.png", dpi=250)

print("--- %s seconds ---" % (time.time() - start_time))
