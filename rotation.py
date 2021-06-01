import cv2
from time import sleep

img = cv2.imread('/home/mr-rider/Robot/book/datasets/misc/house.tiff', 1)
input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows, cols, channel = img.shape
angle = 0

while(1):
    if angle == 360:
        angle = 0
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 0.5)
    rotated = cv2.warpAffine(input, M, (cols, rows))
    cv2.imshow('Rotating Image', rotated)
    angle = angle + 1
    sleep(0.2)
    if cv2.waitKey(1) == 27: # ESC
        break

cv2.destroyAllWindows()