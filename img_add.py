import cv2

img1 = cv2.imread("CV2/1-500x250-3.jpg")
img2 = cv2.imread("CV2/2-500x250-2.jpg")

nwimg = cv2.addWeighted(img1 , 0.9 , img2 , 0.1 , 0)
cv2.imshow("nwimg0",nwimg)
cv2.waitKey(0)