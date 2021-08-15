# author: sbaidya
# date: 08.14.2021

import os

import cv2 as cv

from func import dilation_horizontal, erosion_vertical


def box_extractor(image, index):
    file_path = 'extracted'
    if (index == 1):
        # create initial file path directory
        try:
            os.mkdir(file_path)
        except OSError as error:
            print(error)

    # create page path directory
    page_path = str(file_path)+'/page_'+str(index)
    try:
        os.mkdir(page_path)
    except OSError as error:
        print(error)

    # path for boundary boxes
    boxes_path = str(page_path)+'/boxes'
    try:
        os.mkdir(boxes_path)
    except OSError as error:
        print(error)

    # OPENCV OPERATIONS START
    # cv.namedWindow("output", cv.WINDOW_NORMAL)    # normalize window
    # grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # threshold of the imported image for better detection
    # doc_ref: https://docs.opencv.org/4.5.1/d7/d4d/tutorial_py_thresholding.html
    (thresh, threshImage) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    # viewing threshold image
    # cv.imshow('output', threshImage)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    '''
    values are optimized according to spacing of lines. 
    parameters can be altered by changing the dil_const, and erd_const variables
    '''
    dil_const = 25
    erd_const = 2   # Good for low line spacing. greater means verical loss

    dilatedImage = dilation_horizontal(threshImage, dil_const, 2)
    erodedImage = erosion_vertical(dilatedImage, erd_const, 1)

    '''
    as distances between two lines are too small, this isn't reqd. right now
    adding gaussian blur in the horizontal direction
    '''
    # blur = cv.GaussianBlur(dilatedImage, (35, 1), 1)
    # cv.imshow('output', blur)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    inv_thresh = cv.threshold(erodedImage, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
    # cv.imshow('output', inv_thresh)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # height and width of image
    h, w = inv_thresh.shape

    # doc_ref = https://docs.opencv.org/4.5.2/d9/d61/tutorial_py_morphological_ops.html\
    '''
    kernel width can be set manually.
    here I am using (2 x width) for a generalised solution.
    '''
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2*w, 1))
    dilate = cv.dilate(inv_thresh, kernel, iterations=1)
    # cv.imshow('output', dilate)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # defining contours
    cnts = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv.boundingRect(x)[1])

    count = 1
    json_str = ""
    for c in cnts:
        x, y, w, h = cv.boundingRect(c)
        # condition check to eliminate boxes smaller than 8px in height
        if h > 8:
            roi = image[y:y+h, x:x+w]
            cv.imwrite(str(boxes_path)+'/box'+str(count)+'.jpeg', roi)
            # JSON Generator
            json_str += '"box'+str(count)+'": {\n"top_left": ['+str(y)+', '+str(x)+'],\n"top_right": ['+str(y)+', '+str(w)+'],\n"bottom_left": ['+str(y+h)+', '+str(x)+'],\n"bottom_right": ['+str(y+h)+', '+str(w)+']\n},\n'
            count += 1
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0))

    json_str = '{\n'+json_str[:-2]+'\n}'
    # print(json_str)
    json_file = open(str(page_path)+'/box_map_page_'+str(index)+'.json', 'w')
    n = json_file.write(json_str)
    json_file.close()

    # cv.imshow('output', image)
    cv.imwrite(str(page_path)+'/b_box_page_'+str(index)+'.jpeg', image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()