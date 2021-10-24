import cv2

img =cv2.imread("galaxy.jpg", 1)

print(type(img))

print(img)

print(img.shape)
print(img.ndim)


resizedImage=cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))#bigger!

cv2.imshow("galaxy" ,resizedImage)
cv2.imwrite("Galaxy_Resized.jpg", resizedImage)

cv2.waitKey(2000)#0-until you press a key- 2000 is 2 sec
cv2.destroyAllWindows()
