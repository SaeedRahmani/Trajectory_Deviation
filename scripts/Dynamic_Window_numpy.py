import numpy as np
import matplotlib.pyplot as plt

def dtw_distance(ts_a, ts_b, d=lambda x, y: abs(x - y)):
    # Create cost matrix
    DTW = {}

    for i in range(len(ts_a)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(ts_b)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(ts_a)):
        for j in range(len(ts_b)):
            dist = d(ts_a[i], ts_b[j])
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],    # insertion
                                     DTW[(i, j-1)],    # deletion
                                     DTW[(i-1, j-1)])  # match

    return DTW[len(ts_a)-1, len(ts_b)-1]

# Set the parameters
frequency = 10  # in Hz (points per second)
total_time = 20  # in seconds
num_points = frequency * total_time  # total number of points in each trajectory

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

# Calculate DTW distance
dtw_distance_value = dtw_distance(list(zip(planned_trajectory_x, planned_trajectory_y)),
                                  list(zip(actual_trajectory_x, actual_trajectory_y)))

# Plot the trajectories
plt.figure(figsize=(12, 6))
plt.plot(planned_trajectory_x, planned_trajectory_y, label='Planned Trajectory')
plt.plot(actual_trajectory_x, actual_trajectory_y, label='Actual Trajectory', linestyle='dashed')
plt.title(f'Planned vs Actual Trajectories (DTW Distance: {dtw_distance_value:.2f})')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.grid(True)
plt.show()
