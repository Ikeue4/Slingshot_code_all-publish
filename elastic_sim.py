import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1.0  # Spring constant
m = 1.0  # Mass of the object
x0 = 0.0  # Equilibrium position
initial_displacement = 1.0  # Initial displacement from the equilibrium position
initial_velocity = 0.0  # Initial velocity

# Simulation parameters
dt = 0.01  # Time step
num_steps = 1000   # Number of time steps

# Arrays to store data
positions = np.zeros(num_steps)
energies = np.zeros(num_steps)

# Initialize state
x = x0 + initial_displacement
v = initial_velocity

for step in range(num_steps):
    # Calculate the force (Hooke's Law)
    F = -k * (x - x0)

    # Update the acceleration
    a = F / m

    # Update velocity and position using the Verlet integration method
    x += v * dt + 0.5 * a * dt**2
    v += 0.5 * a * dt

    # Calculate potential energy
    potential_energy = 0.5 * k * (x - x0)**2

    # Store data
    positions[step] = x
    energies[step] = potential_energy

# Plot the results
time = np.arange(0, num_steps) * dt
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, positions)
plt.title('Displacement vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, energies)
plt.title('Potential Energy vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Potential Energy (J)')
plt.grid(True)

plt.tight_layout()
plt.show()
