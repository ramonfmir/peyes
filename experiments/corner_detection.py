import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# How colour changes between two pixels
def colour_change(pixel_a, pixel_b):
	r = pixel_a[0] - pixel_b[0]
	g = pixel_a[1] - pixel_b[1]
	b = pixel_a[2] - pixel_b[2]

	return r*r + g*g + b*b

def get_pixel(image, x, y):
	height, width, _ = image.shape

	if x >= width or y >= height or x < 0 or y < 0:
		return [0, 0, 0]

	return image[y][x]


# Constants
window_width = 5
window_height = 5
v = 2

# Open image
image = ndimage.imread('img1.jpg', mode="RGB")
height, width, _ = image.shape

max_error = 5000

# Core
for window_x in xrange(window_width, width - window_width, window_width):
	for window_y in xrange(window_height, height - window_height, window_height):
		error = 0
		for x in xrange(window_x, window_x + window_width, 1):
			for y in xrange(window_y, window_y + window_height, 1):
				error += colour_change(get_pixel(image, x, y), get_pixel(image, x, y + v))
				error += colour_change(get_pixel(image, x, y), get_pixel(image, x + v, y))

		if error > max_error:
			for i in xrange(window_x, window_x + window_width, 1):
				for j in xrange(window_y, window_y + window_height, 1):
					image[j][i] = [0, 255, 0]

plt.imshow(image)
plt.show()
