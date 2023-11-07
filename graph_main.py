import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

fig, ax = plt.subplots()

def custom_curve(x, a, b, c):
    return a * x**2 + b * x + c

xy = [
    [0,[0]],
    [1,[101.6, 93.2, 105.2, 95.8, 107.4]], 
      [1.5,[105.4, 118.8, 113.2, 107.4, 110.6]], 
      [2,[137.2, 155.2, 164.8, 157.0, 144.4]], 
      [2.5,[151.4, 154.8, 168.2, 174.4, 156.8]], 
      [3,[131.0, 134.2, 143.4, 156.2, 129.6]]
      ]
points = []

for i in xy:
    average = (sum(i[1])//5)
    points.append((i[0], average))

x, y = zip(*points)

# Use curve_fit to fit the custom curve to the data
params, covariance = curve_fit(custom_curve, x, y)

# Extract the fitted parameters
a, b, c = params

# Generate points for the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = custom_curve(x_fit, a, b, c)

ax.plot(x_fit, y_fit, color='red', label='Curve of Best Fit')
ax.plot(x,y, color='blue')
ax.scatter(x,y, label='Slingshot averages')

ax.set_xlabel('Pull Back Distance(cm)')
ax.set_ylabel('Distance Traveled(cm)')
ax.set_title('Slingshot Experiment')
ax.legend()
ax.grid(True)

plt.show()
    