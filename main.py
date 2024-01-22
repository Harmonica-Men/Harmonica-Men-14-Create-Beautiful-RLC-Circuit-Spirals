#
#14-Create-Beautiful--RLC-Circuit-Spirals
#
# CHAPTER 14
#
# "The Earth, that is sufficient, I do not want the consellations any nearer, I know they are very well where they are, I know they suffic for those who belong to them."
#
# -- Walt Whitman, Leaves of Grass, 1855

import random
import matplotlib.pyplot as plt

step_size = 0.1
x, xnew, y = 0, 0, 0

# Seed random number generator
random.seed(123456789)

# Lists to store x and y coordinates for plotting
x_coordinates = []
y_coordinates = []

for j in range(80):
    x = (6. * random.random() / 32767.) - 3
    y = (6. * random.random() / 32767.) - 3

    for i in range(80):
        xnew = x + step_size * y
        y = y + step_size * (-x - y)
        x = xnew

        # Store points for plotting
        x_coordinates.append(x)
        y_coordinates.append(y)

# Plot the points
plt.plot(x_coordinates, y_coordinates, marker='o', linestyle='-')
plt.title('RLC Circuit Spirals')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
