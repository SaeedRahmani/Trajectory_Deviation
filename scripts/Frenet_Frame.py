import numpy as np
import matplotlib.pyplot as plt

def frenet_frame_analysis(planned_x, planned_y, actual_x, actual_y):
    """
    Calculate the lateral (d) and longitudinal (s) displacements in Frenet coordinates.
    """
    # Calculate the differences between the actual and planned trajectories
    dx = actual_x - planned_x
    dy = actual_y - planned_y

    # Calculate the angle of the trajectory
    angles = np.arctan2(np.gradient(planned_y), np.gradient(planned_x))

    # Calculate longitudinal (s) and lateral (d) displacements
    lateral_disp = np.sin(angles) * dx - np.cos(angles) * dy
    longitudinal_disp = np.cos(angles) * dx + np.sin(angles) * dy

    return longitudinal_disp, lateral_disp

# Parameters
frequency = 10  # Hz
total_time = 20  # seconds
num_points = frequency * total_time

# Generate planned trajectory (straight line)
planned_trajectory_x = np.linspace(0, 20, num_points)
planned_trajectory_y = np.linspace(0, 10, num_points)

# Generate actual trajectory
# Starting similar to planned trajectory, then deviating
actual_trajectory_x = np.copy(planned_trajectory_x)
actual_trajectory_y = np.copy(planned_trajectory_y)
deviation_start = num_points // 2
actual_trajectory_y[deviation_start:] += np.linspace(0, 5, num_points - deviation_start)

# Apply Frenet Frame Analysis
longitudinal_disp, lateral_disp = frenet_frame_analysis(planned_trajectory_x, planned_trajectory_y,
                                                        actual_trajectory_x, actual_trajectory_y)

# Plotting
plt.figure(figsize=(12, 6))

# Trajectories
plt.subplot(1, 2, 1)
plt.plot(planned_trajectory_x, planned_trajectory_y, label='Planned Trajectory')
plt.plot(actual_trajectory_x, actual_trajectory_y, label='Actual Trajectory', linestyle='dashed')
plt.title('Planned vs Actual Trajectories')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.grid(True)

# Frenet displacements
plt.subplot(1, 2, 2)
plt.plot(range(num_points), longitudinal_disp, label='Longitudinal Displacement')
plt.plot(range(num_points), lateral_disp, label='Lateral Displacement')
plt.title('Frenet Frame Analysis')
plt.xlabel('Time Step')
plt.ylabel('Displacement')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
