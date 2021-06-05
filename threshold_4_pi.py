import RPi.GPIO as GPIO
import cv2

thresh = 127
cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
button1 = 7
button2 = 11
GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)

while True:
    ret, frame = cap.read()
    button_state = GPIO.input(button1)
    if button_state == GPIO.LOW and thresh < 256:
        thresh = thresh + 1
    ret1, output = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)
    print(thresh)
    cv2.imshow('Thresholding App', output)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()