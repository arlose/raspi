import cv2

cv2.namedWindow("frame", cv2.cv.CV_WINDOW_NORMAL)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
while True:
    frame = cv2.imread('/home/pi/cap.jpg')
    cv2.imshow('frame',frame)
    if 0xff==ord('q'):
        break
cv2.destroyAllWindows()

