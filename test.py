import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 2*np.pi, num=100)
y = np.sin(x)

fig = plt.figure(figsize=(2,3),dpi=200)
plt.plot(x, y)
plt.show()