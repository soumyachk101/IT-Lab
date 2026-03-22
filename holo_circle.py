import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_facecolor('black')

theta = np.linspace(0, 2*np.pi, 100)
x, y = np.cos(theta), np.sin(theta)

for i in range(5):
    alpha = 0.8 - i*0.15
    linewidth = 3 - i*0.4
    ax.plot(x, y, color='cyan', alpha=alpha, linewidth=linewidth)
    x, y = x*1.1, y*1.1

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')
plt.tight_layout()
plt.show()