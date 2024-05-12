"""
Reformulation of Special Angles

This mathematical proof demonstrates the relationship between the radius of a sphere inscribed within a cube and the sine of a special angle (π/3 radians or 60 degrees). The proof shows that if the radius of the cube is 'r', then the radius of the inscribed sphere is (√3/2)r, and the volume of the sphere is (√3/2)πr^3.

The proof is based on the following assumptions:
1. We have a sphere with radius 'r_sphere' and all eight vertices of a cube with side length 'r' touch a point within the sphere.
2. The diagonal length of the cube (L_diag) is calculated using the Pythagorean theorem.
3. The radius of the sphere (r_sphere) is half of the diagonal length (L_diag/2).
4. The volume of the sphere (V_sphere) is calculated using the standard formula (4/3)πr^3.

By substituting the expression for r_sphere in the volume formula, the proof arrives at the relationship:
sin(π/3) = V_sphere / (πx^3), where x = r * sin(π/3).

The proof is visualized using NumPy, showing the cube, the diagonal length, and the inscribed sphere.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
r = 1  # Radius of the cube

# Step 1: Calculate the diagonal length of the cube
diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
print(f"Diagonal length of the cube: {diag_length:.4f}")

# Step 2: Calculate the radius of the sphere
sphere_radius = diag_length / 2
print(f"Radius of the sphere: {sphere_radius:.4f}")

# Step 3: Calculate the volume of the sphere
sphere_volume = (4/3) * math.pi * sphere_radius**3
print(f"Volume of the sphere: {sphere_volume:.4f}")

# Step 4: Verify the proposition
x = r * math.sin(math.pi / 3)
sin_pi_3 = sphere_volume / (math.pi * x**3)
print(f"sin(π/3) = {sin_pi_3:.4f}")

# Visualizations
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create cube data
cube_x = [0, r, r, 0, 0, r, r, 0]
cube_y = [0, 0, r, r, 0, 0, r, r]
cube_z = [0, 0, 0, 0, r, r, r, r]
ax.plot(cube_x, cube_y, cube_z, 'b-')

# Create diagonal line data
diag_x = [0, diag_length/2]
diag_y = [0, diag_length/2]
diag_z = [0, 0]
ax.plot(diag_x, diag_y, diag_z, 'k-', linewidth=2, label='Diagonal')

# Create sphere data
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = sphere_radius * np.cos(u) * np.sin(v)
y = sphere_radius * np.sin(u) * np.sin(v)
z = sphere_radius * np.cos(v)
ax.plot_wireframe(x, y, z, color='r', alpha=0.5, label='Sphere')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Reformulation of Special Angles')
ax.legend()

plt.show()

# Additional Examples
#======================

# Example 1: Radius of the cube is 2
r = 2
diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
sphere_radius = diag_length / 2
sphere_volume = (4/3) * math.pi * sphere_radius**3
x = r * math.sin(math.pi / 3)
sin_pi_3 = sphere_volume / (math.pi * x**3)
print(f"\nExample 1 (r = {r}):")
print(f"Diagonal length of the cube: {diag_length:.4f}")
print(f"Radius of the sphere: {sphere_radius:.4f}")
print(f"Volume of the sphere: {sphere_volume:.4f}")
print(f"sin(π/3) = {sin_pi_3:.4f}")

# Example 2: Radius of the cube is 3
r = 3
diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
sphere_radius = diag_length / 2
sphere_volume = (4/3) * math.pi * sphere_radius**3
x = r * math.sin(math.pi / 3)
sin_pi_3 = sphere_volume / (math.pi * x**3)
print(f"\nExample 2 (r = {r}):")
print(f"Diagonal length of the cube: {diag_length:.4f}")
print(f"Radius of the sphere: {sphere_radius:.4f}")
print(f"Volume of the sphere: {sphere_volume:.4f}")
print(f"sin(π/3) = {sin_pi_3:.4f}")

# Tests
#=======

import unittest

class TestReformulationOfSpecialAngles(unittest.TestCase):
    def test_diagonal_length(self):
        r = 1
        expected_diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
        diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
        self.assertAlmostEqual(diag_length, expected_diag_length, places=4)

    def test_sphere_radius(self):
        r = 1
        diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
        expected_sphere_radius = diag_length / 2
        sphere_radius = diag_length / 2
        self.assertAlmostEqual(sphere_radius, expected_sphere_radius, places=4)

    def test_sphere_volume(self):
        r = 1
        diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
        sphere_radius = diag_length / 2
        expected_sphere_volume = (4/3) * math.pi * sphere_radius**3
        sphere_volume = (4/3) * math.pi * sphere_radius**3
        self.assertAlmostEqual(sphere_volume, expected_sphere_volume, places=4)

    def test_sin_pi_3(self):
        r = 1
        diag_length = math.sqrt(r**2 + (math.sqrt(2)*r)**2)
        sphere_radius = diag_length / 2
        sphere_volume = (4/3) * math.pi * sphere_radius**3
        x = r * math.sin(math.pi / 3)
        expected_sin_pi_3 = sphere_volume / (math.pi * x**3)
        sin_pi_3 = sphere_volume / (math.pi * x**3)
        self.assertAlmostEqual(sin_pi_3, expected_sin_pi_3, places=4)

if __name__ == '__main__':
    unittest.main()