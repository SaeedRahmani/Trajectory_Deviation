import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
frequency = 10  # in Hz (points per second)
total_time = 20  # in seconds
num_points = frequency * total_time  # total number of points in each trajectory

# Time vector
time_vector = np.linspace(0, total_time, num_points)

# Generate the planned trajectory (straight line)
planned_trajectory_x = np.linspace(0, 20, num_points)
planned_trajectory_y = np.linspace(0, 10, num_points)

# Generate the actual trajectory (matches planned for the first 10 seconds, then deviates)
actual_trajectory_x = np.copy(planned_trajectory_x)
actual_trajectory_y = np.copy(planned_trajectory_y)
deviation_point = frequency * 10  # The point at which deviation starts

# Introduce deviation in the y-coordinate after 10 seconds
for i in range(deviation_point, num_points):
    actual_trajectory_y[i] += (i - deviation_point) * 0.05  # Gradual deviation

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Array to store the deviation distances
deviation_distances = np.zeros(num_points)

# Calculating the deviation for each point in time
for i in range(num_points):
    deviation_distances[i] = euclidean_distance(planned_trajectory_x[i], planned_trajectory_y[i],
                                                actual_trajectory_x[i], actual_trajectory_y[i])

# Plotting the trajectories and deviations
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(planned_trajectory_x, planned_trajectory_y, label='Planned Trajectory')
plt.plot(actual_trajectory_x, actual_trajectory_y, label='Actual Trajectory', linestyle='dashed')
plt.title('Planned vs Actual Trajectories')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(time_vector, deviation_distances, label='Deviation')
plt.title('Deviation Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Deviation Distance')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
