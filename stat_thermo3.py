import numpy as np
import matplotlib.pyplot as plt

theta_vib = 1500 
theta_rot = 15

v = np.arange(0, 10)
J = np.arange(0, 30)

T_vib_low = 300
T_vib_high = 2000

T_rot_low = 50
T_rot_high = 300

# 2c) Harmonischer Oszillator: n_v / n_0 = exp(-v * theta_vib / T)
osc_low = np.exp(-v * theta_vib / T_vib_low)
osc_high = np.exp(-v * theta_vib / T_vib_high)

# 2e) Starrer Rotator: n_J / n_0 = (2J + 1) * exp(-J*(J+1) * theta_rot / T)
rot_low = (2 * J + 1) * np.exp(-J * (J + 1) * theta_rot / T_rot_low)
rot_high = (2 * J + 1) * np.exp(-J * (J + 1) * theta_rot / T_rot_high)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 2c: Harmonischer Oszillator
ax1.plot(v, osc_low, marker='o', linestyle='-', label=f'Niedrige T ({T_vib_low} K)')
ax1.plot(v, osc_high, marker='s', linestyle='-', label=f'Hohe T ({T_vib_high} K)')
ax1.set_title('2c) Harmonischer Oszillator\n(ohne Entartung)')
ax1.set_xlabel('Schwingungsquantenzahl $v$')
ax1.set_ylabel(r'Besetzungsverhältnis $n_v / n_0$')
ax1.set_xticks(v)
ax1.grid(True, alpha=0.3)
ax1.legend()

# Subplot 2e: Starrer Rotator
ax2.plot(J, rot_low, marker='o', linestyle='-', label=f'Niedrige T ({T_rot_low} K)')
ax2.plot(J, rot_high, marker='s', linestyle='-', label=f'Hohe T ({T_rot_high} K)')
ax2.set_title('2e) Starrer Rotator\n(mit Entartung $g_J = 2J+1$)')
ax2.set_xlabel('Rotationsquantenzahl $J$')
ax2.set_ylabel(r'Besetzungsverhältnis $n_J / n_0$')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()