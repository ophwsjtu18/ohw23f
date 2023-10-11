import cv2

img = cv2.imread('homework1_1_img.jpg')
for x in range(3):
    for y in range(3):
        cv2.rectangle(img, (x*60, y*50), (x*60+60, y*50+50), (0, 255, 0), 3)
cv2.imshow('image',img)
print(img.shape)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cv2.imwrite('homework1_2_img.jpg',img)