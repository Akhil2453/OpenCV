# First OpenCV program
# This program is used to read, display and write an image


#import the OpenCV library
import cv2
#import the numpy library (used to dtore the images)
import numpy as np 

#cv2.imread, reads an image, from the path given
img = cv2.imread('input.jpg')

#cv2.imshow, display the image, stored in the varable created
# it take sin two arguments
cv2.imshow('Hello World', img)

#this function is used to display the image for certain period
#if no argument is given the, program waits till any key is pressed
cv2.waitKey()

#this closes all open windows
#an important function, failed to call your program will get hanged
cv2.destroyAllWindows()