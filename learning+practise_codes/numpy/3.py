import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 20)
print(x)
array = np.arange(10, dtype=np.int64)
array = array.reshape((5, 2))
print(array)
plt.plot(array)
plt.show()

