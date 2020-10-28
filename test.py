import numpy as np
import matplotlib.pyplot as plt
import json

# x = np.linspace(1, 2*np.pi, num=100)
# y = np.sin(x)

# fig = plt.figure(figsize=(2,3),dpi=200)
# plt.plot(x, y)
# plt.show()

with open('/Users/beltranscg/Desktop/PhD/Year1/PhD_YEAR_1/MODTRAN6.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)