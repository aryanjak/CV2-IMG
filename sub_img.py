import cv2

img0 = cv2.imread("CV2/star-1-300x168.jpg")
img1 = cv2.imread("CV2/dot-300x168.jpg")

nwimg = cv2.subtract(img0 , img1)
cv2.imshow("new",nwimg)
cv2.waitKey(0)