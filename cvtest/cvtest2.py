import cv2

s1 = cv2.imread('c1.jpg')
s2 = cv2.imread("c2.jpg")

diff=cv2.absdiff(s1,s2)

r,c_img = cv2.threshold(diff,80,255,cv2.THRESH_BINARY)
gray=cv2.cvtColor(c_img,cv2.COLOR_BGR2GRAY)

canny=cv2.Canny(diff,100,200)
cont,r2 =cv2.findContours(gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow("diff", diff)

for a in cont:
	x,y,w,h = cv2.boundingRect(a)
	cv2.rectangle(c_img,(x,y),(x+w,y+h),(255,0,0),2)
	
	
cv2.imshow("THRESH",c_img)

cv2.waitKey()

