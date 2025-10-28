import cv2

image = cv2.imread("PIG.png")

cv2.imshow("pig", image)
cv2.waitKey(0)

resize = cv2.resize(image, (600,600))
cv2.imshow("Big Pig", resize)
cv2.waitKey(0)

cv2.destroyAllWindows()