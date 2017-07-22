import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
import numpy as np

f = open('dat.txt', 'r')
x = []
y = []
i = 0
for line in f.readlines():
	lst = line.split(' ')
	x.append(i)
	y.append(float(lst[len(lst)-1]))
	i += 100

x = np.array(x)
y = np.array(y)

yy_sg = savgol_filter(y, 53, 3)

red_patch = mpatches.Patch(color='red', label='Savitzky-Golay')
xd = plt.legend(loc=4, handles=[red_patch])

ax = plt.gca().add_artist(xd)


blue_patch = mpatches.Patch(color='blue', label='Unchanged Trend Line')
plt.legend(loc=1, handles=[blue_patch])

plt.plot(x, y)
plt.xlabel('Iterations')
plt.ylabel('Accuracy')
plt.plot(x, yy_sg, c='r')
plt.show()
print(np.max(yy_sg))
