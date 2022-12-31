# Importing all modules
import cv2 as cv
import numpy as np

# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([120, 100, 20])
upper = np.array([140, 255, 255]) # (These ranges will detect purple)

img1 = cv.imread('color_pencils.jpeg')

img = cv.cvtColor(img1, cv.COLOR_BGR2HSV) # Converting BGR image to HSV format

mask = cv.inRange(img, lower, upper) # Masking the image to find our color

mask_contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

# Finding position of all contours
if len(mask_contours) != 0:
    for mask_contour in mask_contours:
        if cv.contourArea(mask_contour) > 500:
            x, y, w, h = cv.boundingRect(mask_contour)
            cv.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle

    cv.imshow("mask image", mask) # Displaying mask image

    cv.imshow("inputed image", img1) # Displaying webcam image

    cv.waitKey(0)
