import cv2
koya = cv2.imread("koya.png")
cv2.imshow("grey koya",koya)

koya = cv2.imread('koya.png')
rows,columns = koya.shape[:2]
for i in range(rows) : 
    for j in range(columns) : 
        koya[i,j]=sum(koya[i,j])*0.17
cv2.imshow("grey koya",koya)
cv2.waitKey(0)

cv2.destroyAllWindows()