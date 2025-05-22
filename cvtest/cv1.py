import cv2

img = cv2.imread('c1.jpg')
#cimg=cv2.GaussianBlur(img,(7,7),0)
#r,cimg=cv2.threshold(img, 120, 255 ,cv2.THRESH_BINARY)
cimg = cv2.Canny(img,100,200)

cv2.imshow("",img)
cv2.imshow("converted",cimg)
cv2.waitKey(0)
