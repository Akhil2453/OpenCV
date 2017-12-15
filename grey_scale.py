#an alternate method to convert image into greyscale

import cv2

img = cv2.imread('input.jpg', 0)

cv2.imshow('GrayScale', img)
cv2.waitKey()
cv2.destroyAllWindows()