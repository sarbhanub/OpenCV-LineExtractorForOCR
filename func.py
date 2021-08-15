# author: sbaidya
# date: 08.04.2021
# updated: 08.14.2021

# important_functions

import cv2 as cv
import numpy as np

# function to crop my image
def crop(image, y, x, h, w):
    cropped_image = image[y:y + h, x:x + w]
    return cropped_image

# thickens the font# second parameter for the level
def dilation(image, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv.dilate(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image

# thinness the font # second parameter for the level
def erosion(image, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv.erode(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image

# removes noise # using morphology
# value = effect of smoothing # weight = adds blur
def remove_noise(image, value, weight):
    kernel = np.ones((1, 1), np.uint8)
    image = cv.dilate(image, kernel, iterations=value)
    kernel = np.ones((1, 1), np.uint8)
    image = cv.erode(image, kernel, iterations=value)
    image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    image = cv.GaussianBlur(image, (7,7), 2)
    return image


# Horizontal expansion # val defines the power # iteration defines no. of pass
def dilation_horizontal(image, val, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((1, val), np.uint8) # val x 1 matrix
    image = cv.dilate(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image

# vertical expansion # val defines the power # iteration defines no. of pass
def dilation_vertical(image, val, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((val, 1), np.uint8) # 1 x val matrix
    image = cv.dilate(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image


# Horizontal compression # val defines the power # iteration defines no. of pass
def erotion_horizontal(image, val, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((1, val), np.uint8)
    image = cv.erode(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image

# vertical compression # val defines the power # iteration defines no. of pass
def erosion_vertical(image, val, iteration):
    image = cv.bitwise_not(image)
    kernel = np.ones((val, 1), np.uint8)
    image = cv.erode(image, kernel, iterations=iteration)
    image = cv.bitwise_not(image)
    return image