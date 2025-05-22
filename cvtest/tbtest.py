import cv2

def nothing(x):
    pass

title = 'Trackbar Threshold'
cv2.namedWindow(title)

cv2.createTrackbar('Threshold', title, 0, 255, nothing)


img = cv2.imread('c1.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("no")
    exit()

while True:
    
    thresh = cv2.getTrackbarPos('Threshold', title)

    
    _, cimg = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    
    cv2.imshow(title, cimg)

    
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()
