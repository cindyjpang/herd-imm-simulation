import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation 

fig, ax = plt.subplots()
fig.set_tight_layout(True)

print('fig size: {0} DPI, size in inches {1}'.format(fig.get_dpi(), fig.get_size_inches()))

x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 2.0, len(x)))
line,  = ax.plot(x, x-5, 'r', linewidth = 2)

plt.show()