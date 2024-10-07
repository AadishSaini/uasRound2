import cv2 as cv
import numpy as np 
from consts import *
from tools import *


#create a blank blue and yellow screen
blue_screen = np.full((640, 640, 3), (255, 255, 0), dtype=np.uint8)
yellow_screen = np.full((640, 640, 3), (0, 255, 255), dtype=np.uint8)


# loop through the images
for itr in range(1, 12):

    #get the tools class file
    t = tools()


    # no 9.png in the images folder
    if itr == 9:
        continue

    # load the image
    filePath = "./images/"+str(itr)+".png"
    image = cv.imread(filePath)

    
    #convert image to hsv
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)


    #get masked images for different colours in the origional image and assign different colours to them,
    # green ----> blue
    # brown ----> yellow
    # red, blue = red, blue
    green_masked_image = t.create_mask(hsv_image, GREEN_LOWER_HSV, GREEN_UPPER_HSV, blue_screen)
    brown_masked_image = t.create_mask(hsv_image, BROWN_LOWER_HSV, BROWN_UPPER_HSV, yellow_screen)
    blue_pointer_masked_image = t.create_mask(hsv_image, BLUE_POINTER_LOWER_HSV, BLUE_POINTER_UPPER_HSV, image)
    red_pointer_masked_image = t.create_mask(hsv_image, RED_POINTER_LOWER_HSV, RED_POINTER_UPPER_HSV, image)
    

    # add all the masked images to a single image to get the output image
    output_image = t.total_image(green_masked_image, brown_masked_image, blue_pointer_masked_image, red_pointer_masked_image)



    # get the contours (boxes around different pointers) and get the surrounding colours of it
    red_arr_colours = t.give_contour_and_surrounding_colour(red_pointer_masked_image, output_image, output_image)
    blue_arr_colours = t.give_contour_and_surrounding_colour(blue_pointer_masked_image, output_image, output_image)


    # calculate the number of pointers in different areas by seeing and comparing colours near the contour
    (red_in_brown, red_in_green, blue_in_brown, blue_in_green) = t.calculate_numbers(red_arr_colours, blue_arr_colours)


    # finding outputs
    hb = red_in_brown+blue_in_brown
    hg = red_in_green+blue_in_green
    house_list = [hb, hg]
    pb = red_in_brown + (blue_in_brown*2)
    pg = red_in_green + (blue_in_green*2)
    pr = pb/pg

    #show the output image
    cv.imshow('window', output_image)

    # end for one image
    cv.waitKey(0)
    cv.destroyAllWindows()
