import cv2

#load input image

image = cv2.imread('input.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

#Use cvtColor, to cnvert into grayscale
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	

cv2.imshow('Grayscale', grayimg)
cv2.waitKey()
cv2.destroyAllWindows()