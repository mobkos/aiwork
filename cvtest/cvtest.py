import cv2

def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow("mycamera")
cv2.createTrackbar('Threshold', 'mycamera', 127, 255, nothing)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    thresh = cv2.getTrackbarPos('Threshold', 'mycamera')
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(g, thresh, 255, cv2.THRESH_BINARY)
    cv2.imshow("mycamera", binary)

    if cv2.waitKey(1) == 27:
        break


cam.release()
cv2.destroyAllWindows()
