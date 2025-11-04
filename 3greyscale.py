import cv2
pig = cv2.imread("PIG.png")
cv2.imshow("grey pig",pig)

#
rows,columns = pig.shape[:2]

for i in range(rows) : 
    for j in range(columns) : 
        pig[i,j]=sum(pig[i,j])*0.17



cv2.imshow("grey pig",pig)
cv2.waitKey(0)
cv2.destroyAllWindows 