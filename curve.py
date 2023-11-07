import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

xy = [[1,[101.6, 93.2, 105.2, 95.8, 107.4]], [1.5,[105.4, 118.8, 113.2, 107.4, 110.6]], [2,[137.2, 155.2, 164.8, 157.0, 144.4]], [2.5,[151.4, 154.8, 168.2, 174.4, 156.8]], [3,[131.0, 134.2, 143.4, 156.2, 129.6]]]
points_max = []
points_min = []
fig, ax = plt.subplots()

for i in xy:
    min_num = min(i[1])
    max_num = max(i[1])
    print(max_num, min_num)
    points_max.append((max_num, i[0]))
    points_min.append((min_num, i[0]))

y, x = zip(*points_max)
spl = make_interp_spline(x, y)
xnew = np.linspace(min(x), max(x), 500)
ax.plot(xnew, spl(xnew))

y, x = zip(*points_min)
spl = make_interp_spline(x, y)
xnew = np.linspace(min(x), max(x), 500)
ax.plot(xnew, spl(xnew))

x = [1, 1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 2, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 3]
y = [101.6, 93.2, 105.2, 95.8, 107.4, 105.4, 118.8, 113.2, 107.4, 110.6, 137.2, 155.2, 164.8, 157.0, 144.4, 151.4, 154.8, 168.2, 174.4, 156.8, 131.0, 134.2, 143.4, 156.2, 129.6]
    
ax.scatter(x, y, label='Data')

plt.show()
