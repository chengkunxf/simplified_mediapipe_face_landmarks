import cv2
import numpy as np

img = cv2.imread('images/face_shape.png')

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh_img = cv2.threshold(img_grey, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# create an empty image for contours
img_contours = np.zeros(img.shape)

# draw the contours on the empty image
# cv2.drawContours(img_contours, contours[0], -1, (0, 255, 0), 3)

approxs1 = cv2.approxPolyDP(contours[0], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('0-facial', img_contours)

approxs1 = cv2.approxPolyDP(contours[2], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('2-lips', img_contours)

approxs1 = cv2.approxPolyDP(contours[4], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('4-nose', img_contours)

approxs1 = cv2.approxPolyDP(contours[6], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('6-righteye', img_contours)

approxs1 = cv2.approxPolyDP(contours[8], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('8-lefteye', img_contours)

approxs1 = cv2.approxPolyDP(contours[10], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('10-rightbrow', img_contours)

approxs1 = cv2.approxPolyDP(contours[12], 1, True)
cv2.polylines(img_contours, [approxs1], True, (255, 255, 255), 1)
cv2.imshow('12-leftbrow', img_contours)

cv2.waitKey()
cv2.destroyAllWindows()
