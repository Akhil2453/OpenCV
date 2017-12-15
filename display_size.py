#This program displays the size of the image

import cv2

import numpy as np 

img = cv2.imread('input.jpg')

print img.shape			#prints the height and width of the image in pixels

print "The height of the image is ", int(img.shape[0]), "pixels"
print "The width of the image is ", int(img.shape[1]), "pixels"