# author: sbaidya
# date: 08.14.2021

# this will convert the given pdf into image files and save them in a directory
import os
import cv2 as cv
from pdf2image import convert_from_path
from extractor import box_extractor

# extracted jpeg(s) directory
jpeg_path = 'data/jpeg'
try:
    os.mkdir(jpeg_path)
except OSError as error:
    print(error)

pdf = convert_from_path('data/doc/Sanskrit_Text.pdf')
index = 0

for page in pdf:
     index += 1
     page.save('data/jpeg/page_'+str(index)+'.jpeg', 'JPEG')

print('Total no. of pages: '+str(index))

# will create the files for the pages
for pg in range(1, index+1):
    image = cv.imread('data/jpeg/page_'+str(pg)+'.jpeg')
    box_extractor(image, pg)