import numpy as np
import matplotlib.pyplot as plt

g = np.linspace(-100, 100, 2000)
A0 = np.zeros_like(g)

# Bereich g < -1
mask1 = g < -1
A0[mask1] = -np.sqrt(-1 - g[mask1]) * 1/np.tanh(np.pi/2 * np.sqrt(-1 - g[mask1]))

# Bereich g > -1
mask2 = g > -1
A0[mask2] = -np.sqrt(1 + g[mask2]) * 1/np.tan(np.pi/2 * np.sqrt(1 + g[mask2]))

# Polstellen maskieren für besseren Plot
threshold = 20
A0[A0 > threshold] = np.nan
A0[A0 < -threshold] = np.nan

plt.figure(figsize=(10, 6))
plt.plot(g, A0, label='$A_0(g)$', color='blue')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(-1, color='red', linestyle='--', label='g = -1', alpha=0.5)
plt.ylim(-10, 10)
plt.xlim(-100, 100)
plt.xlabel('g')
plt.ylabel('$A_0(g)$')
plt.title('Verlauf der Streulänge $A_0(g)$')
plt.grid(False)
plt.legend()
plt.show()