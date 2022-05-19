import cv2

img0 = cv2.imread("CV2/1-500x250-3.jpg")
startpoint = (0,0)
endpoint = (200 , 200)
color = (0,255,0)
thikness = (9)
newimg = cv2.line(img0,startpoint,endpoint,color,thikness)
cv2.imshow("HI",newimg)
cv2.waitKey(0)