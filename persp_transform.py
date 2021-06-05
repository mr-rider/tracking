import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('/home/mr-rider/Robot/book/datasets/misc/ruler.512.tiff', 1)
input_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rows, cols, channels = input_image.shape

points1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
points2 = np.float32([[0,0], [200, 0], [0, 300], [300, 300]])

P = cv2.getPerspectiveTransform(points1, points2)
output = cv2.warpPerspective(input_image, P, (300, 300))

plt.subplot(121)
plt.imshow(input_image)
plt.title('Input Image')

plt.subplot(122)
plt.imshow(output)
plt.title('Perspective Transform')
plt.show()