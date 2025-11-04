import cv2

pig = cv2.imread("PIG.png")

#HUE Saturation Values

hsvimage = cv2.cvtColor(pig, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV PIG", hsvimage)

cv2.waitKey(0)
cv2.destroyAllWindows()