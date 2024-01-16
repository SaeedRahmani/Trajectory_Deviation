import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

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

# Combine x and y coordinates into tuples for DTW
planned_trajectory = np.array(list(zip(planned_trajectory_x, planned_trajectory_y)))
actual_trajectory = np.array(list(zip(actual_trajectory_x, actual_trajectory_y)))

# Apply Dynamic Time Warping (DTW)
distance, path = fastdtw(planned_trajectory, actual_trajectory, dist=euclidean)

# Plot the trajectories
plt.figure(figsize=(12, 6))
plt.plot(planned_trajectory_x, planned_trajectory_y, label='Planned Trajectory')
plt.plot(actual_trajectory_x, actual_trajectory_y, label='Actual Trajectory', linestyle='dashed')
plt.title('Planned vs Actual Trajectories (DTW Distance: {:.2f})'.format(distance))
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.grid(True)
plt.show()
