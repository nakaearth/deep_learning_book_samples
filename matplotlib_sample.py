import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y  = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y, label="sin")
plt.plot(x, y2, linestyle ="--", label="cos")
plt.xlabel("X")
plt.xlabel("Y")
plt.title("sin & cos")
plt.legend()
plt.show()
