import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('/home/mr-rider/Robot/book/datasets/misc/4.2.06.tiff', 1)
input_image = cv2. cvtColor(image, cv2.COLOR_BGR2RGB)
rows, cols, channels = input_image.shape

points1 = np.float32([[100, 100], [300, 100], [100, 300]])
points2 = np.float32([[200, 150], [400, 150], [100, 300]])

A = cv2.getAffineTransform(points1, points2)
output = cv2.warpAffine(input_image, A, (cols, rows))

plt.subplot(121)
plt.imshow(input_image)
plt.title('Input')

plt.subplot(122)
plt.imshow(output)
plt.title('Affine Output')
plt.show()