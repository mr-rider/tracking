import cv2


def emptyFunction():
    pass


thresh = 127
cap = cv2.VideoCapture(0)

windowName = 'Object Tracker'
trackbarName = 'Chooser'

cv2.namedWindow(windowName)
cv2.createTrackbar(trackbarName, windowName, 0, 2, emptyFunction)


while True:
    ret, frame = cap.read()
    button_state = cv2.getTrackbarPos(trackbarName, windowName)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if button_state == 0 and thresh < 256:
        thresh = thresh + 1
    if button_state == 2 and thresh > -1:
        thresh = thresh - 1

    ret1, output = cv2.threshold(gray_frame, thresh, 255, cv2.THRESH_BINARY)
    print(thresh)
    cv2.imshow(windowName, output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()