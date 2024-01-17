import numpy as np
import matplotlib.pyplot as plt

# Set parameters
frequency = 10  # Hz
total_time = 20  # seconds
num_points = frequency * total_time

# Time vector for plotting
time_vector = np.linspace(0, total_time, num_points)

# Generate planned trajectory (straight line with constant speed)
planned_trajectory_x = np.linspace(0, 20, num_points)
planned_trajectory_y = np.linspace(0, 10, num_points)
planned_speed = np.full(num_points, 5)  # Constant speed

# Generate actual trajectory (similar to planned initially, then deviates)
actual_trajectory_x = np.copy(planned_trajectory_x)
actual_trajectory_y = np.copy(planned_trajectory_y)
actual_speed = np.random.normal(5, 1, num_points)  # Speed with random variation

# Deviation points
deviation_point = frequency * 10
actual_trajectory_y[deviation_point:] += np.linspace(0, 5, num_points - deviation_point)

# Function to calculate deviations
def calculate_deviations(planned, actual):
    return np.abs(planned - actual)

# Calculate deviations
deviation_x = calculate_deviations(planned_trajectory_x, actual_trajectory_x)
deviation_y = calculate_deviations(planned_trajectory_y, actual_trajectory_y)
deviation_speed = calculate_deviations(planned_speed, actual_speed)

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(12, 18))

# Trajectories with speed color
sc1 = axs[0].scatter(planned_trajectory_x, planned_trajectory_y, c=planned_speed, cmap='viridis', label='Planned Trajectory')
sc2 = axs[0].scatter(actual_trajectory_x, actual_trajectory_y, c=actual_speed, cmap='viridis', label='Actual Trajectory')
fig.colorbar(sc1, ax=axs[0], label='Speed')
axs[0].set_title('Trajectories with Speed Color')
axs[0].set_xlabel('X Position')
axs[0].set_ylabel('Y Position')
axs[0].legend()

# Deviations in X and Y
axs[1].plot(time_vector, deviation_x, label='Deviation in X')
axs[1].plot(time_vector, deviation_y, label='Deviation in Y')
axs[1].set_title('Deviations in X and Y')
axs[1].set_xlabel('Time (seconds)')
axs[1].set_ylabel('Deviation')
axs[1].legend()

# Deviations of Speed
axs[2].plot(time_vector, deviation_speed, label='Deviation of Speed', color='red')
axs[2].set_title('Deviations of Speed')
axs[2].set_xlabel('Time (seconds)')
axs[2].set_ylabel('Speed Deviation')
axs[2].legend()

plt.tight_layout()
plt.show()
