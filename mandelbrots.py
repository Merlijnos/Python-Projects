import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.ndimage import gaussian_filter


# Define the function to generate the fractal
def mandelbrot(c, max_iter):
    z = np.zeros_like(c)
    n = np.zeros_like(c, dtype=np.int32)
    for i in range(max_iter):
        z = z**2 + c
        mask = abs(z) > 2
        n[mask] = i
        z[mask] = np.nan
    return n


# Set the number of iterations and the resolution of the plot
max_iter = 100
resolution = 1000

# Set the random seed based on the current time
np.random.seed(int(time.time()))

# Generate a random range for the plot
x_min, x_max = np.random.uniform(-2, 1), np.random.uniform(-2, 1)
y_min, y_max = np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5)

# Generate the fractal
x = np.linspace(x_min, x_max, resolution)
y = np.linspace(y_min, y_max, resolution)
X, Y = np.meshgrid(x, y)
C = X + Y * 1j

Z = C.copy()
M = mandelbrot(C, max_iter)

for i in range(max_iter):
    Z = Z**2 + C
    mask = abs(Z) > 2
    Z[mask] = np.nan

# Apply a Gaussian blur filter to the image
M_blur = gaussian_filter(M, sigma=5)

# Invert the colors of the image
M_invert = 1 - M_blur

# Plot the filtered and transformed image
plt.figure(figsize=(10, 10))
plt.imshow(M_invert, cmap="magma", extent=(x_min, x_max, y_min, y_max))
plt.axis("off")
plt.show()
