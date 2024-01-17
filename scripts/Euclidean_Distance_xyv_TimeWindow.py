import numpy as np
import matplotlib.pyplot as plt

# Set parameters
frequency = 10  # Hz
total_time = 20  # seconds
num_points = frequency * total_time
time_window = 5  # Time window for checking consecutive deviations

# Generate planned and actual trajectories
planned_trajectory_x = np.linspace(0, 20, num_points)
planned_trajectory_y = np.linspace(0, 10, num_points)
planned_speed = np.full(num_points, 5)  # Constant speed

actual_trajectory_x = np.copy(planned_trajectory_x)
actual_trajectory_y = np.copy(planned_trajectory_y)
actual_speed = np.random.normal(5, 1, num_points)  # Speed with random variation

# Introduce deviation in the y-coordinate after 10 seconds
deviation_point = frequency * 10
actual_trajectory_y[deviation_point:] += np.linspace(0, 5, num_points - deviation_point)

# Calculate deviations
deviation_x = np.abs(planned_trajectory_x - actual_trajectory_x)
deviation_y = np.abs(planned_trajectory_y - actual_trajectory_y)
deviation_speed = np.abs(planned_speed - actual_speed)

# Identify problematic areas
problematic = np.zeros(num_points, dtype=bool)
for i in range(num_points - time_window + 1):
    if (np.all(deviation_x[i:i+time_window] > 1) or 
        np.all(deviation_y[i:i+time_window] > 2) or
        np.all(deviation_speed[i:i+time_window] > 0.5)):
        problematic[i:i+time_window] = True

# Adjusting the figure size for better display
fig, axs = plt.subplots(3, 1, figsize=(6, 8))  # Reduced figure size

# Trajectories with speed color
sc1 = axs[0].scatter(planned_trajectory_x, planned_trajectory_y, c=planned_speed, cmap='viridis', label='Planned Trajectory')
sc2 = axs[0].scatter(actual_trajectory_x, actual_trajectory_y, c=actual_speed, cmap='viridis', label='Actual Trajectory')
fig.colorbar(sc1, ax=axs[0], label='Speed')
axs[0].set_title('Trajectories with Speed Color')
axs[0].set_xlabel('X Position')
axs[0].set_ylabel('Y Position')
axs[0].legend()

# Deviations in X and Y
axs[1].plot(deviation_x, label='Deviation in X')
axs[1].plot(deviation_y, label='Deviation in Y')
axs[1].set_title('Deviations in X and Y')
axs[1].set_xlabel('Time (seconds)')
axs[1].set_ylabel('Deviation')
axs[1].legend()

# Deviations of Speed with problematic areas highlighted
for i in range(num_points):
    if problematic[i]:
        axs[2].scatter(i/frequency, deviation_speed[i], color='red')  # Highlight problematic areas in red
    else:
        axs[2].scatter(i/frequency, deviation_speed[i], color='blue')  # Non-problematic areas in blue

axs[2].set_title('Deviations of Speed with Problematic Areas Highlighted')
axs[2].set_xlabel('Time (seconds)')
axs[2].set_ylabel('Speed Deviation')

plt.tight_layout()
plt.show()
