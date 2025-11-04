import cv2

pig = cv2.imread('PIG.png')
cv2.imshow("PIG", pig)
rows,columns = pig.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
rotatedpig = cv2.getRotationMatrix2D((columns/2,rows/2), 78, 1)
resolution = cv2.warpAffine(pig, rotatedpig, (columns, rows))
cv2.imshow("rotated pig", resolution)

cv2.waitKey(0)
cv2.destroyAllWindows()
