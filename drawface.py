# python version 3.9.7
# opncv-python version = 4.5.4.60
# mediapipe version = 0.8.9.1

import cv2
from mpFaceSimplified import mpFace
import numpy as np

img = cv2.imread("f_hair_1.jpg")
cv2.imshow('img', img)

size = img.shape
width = size[1]
height = size[0]
img_black = np.zeros(img.shape)

radius = 2
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
yellow = (0, 255, 255)
white = (255, 255, 255)

faceLm = mpFace(width, height)


# For connecting range of dots
def connectPoints(indx1, indx2):
    for i in range(indx1, indx2):
        if i == (indx2 - 1):
            cv2.line(img_black, (face[i][0], face[i][1]), (face[indx1][0], face[indx1][1]), white, 3)
            break
        cv2.line(img_black, (face[i][0], face[i][1]), (face[i + 1][0], face[i + 1][1]), white, 3)


faces = faceLm.faceLandmarksSimplified(img)

for face in faces:
    connectPoints(0, 10)  # Left Eyebrow (0->9)
    connectPoints(10, 20)  # right Eyebrow (10->19)
    connectPoints(20, 36)  # Left Eye (20->35)
    connectPoints(36, 52)  # Right Eye (36->51)
    # connectPoints(52,72)#iner Lip (52->71)
    connectPoints(52, 72)  # outer Lip (52->72)
    connectPoints(72, 108)  # face boundary (72->107)
    connectPoints(118, 137)  # face boundary (118->136)

cv2.imshow('Webcam', img_black)

cv2.waitKey()
cv2.destroyAllWindows()
