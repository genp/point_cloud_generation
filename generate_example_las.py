import numpy as np
import laspy

# Generate synthetic point cloud data
num_points = 10000
x = np.random.uniform(0, 100, num_points)
y = np.random.uniform(0, 100, num_points)
z = 5 * np.sin(0.1 * x) + 5 * np.cos(0.1 * y) + np.random.normal(0, 0.5, num_points)

# Create LAS header
header = laspy.LasHeader(point_format=3, version="1.2")
header.offsets = [0.0, 0.0, 0.0]
header.scales = [0.01, 0.01, 0.01]

# Create LAS file
las = laspy.LasData(header)
las.x = x
las.y = y
las.z = z

# Write to file
las.write("example_random.las")
print("example.las written with", num_points, "points.")
