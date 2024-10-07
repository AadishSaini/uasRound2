import cv2 as cv
import numpy as np
from consts import *

class tools:
    def __init__(self):
        pass
    
    #masking function to seperate different colours in the image
    def create_mask(self, image, LOWER, UPPER, output_screen):
        # get lower and upper limits of color values to be included in mask
        lower = np.array(LOWER)
        upper = np.array(UPPER)

        #create mask
        mask = cv.inRange(image, lower, upper)

        # put the mask on the required colour
        result_green_mask = cv.bitwise_and(output_screen, output_screen, mask=mask)
        return result_green_mask
    
    # create the output image
    def total_image(self, img1, img2, img3, img4):
        # add the images one by one 
        result1 = cv.addWeighted(img1, 1, img2, 1, 0)
        result2 = cv.addWeighted(img3, 1, result1, 1, 0)
        result = cv.addWeighted(img4, 1, result2, 1, 0)
        return result
    
    # create boundaries around the pointers, and consequtively find the surrounding colour
    def give_contour_and_surrounding_colour(self, masked_image, to_mask_on, converted_image):
        #convert image to grayscale then apply threshhold
        gray_image = cv.cvtColor(masked_image, cv.COLOR_BGR2GRAY)
        _, thresholded_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY)

        #get contours surrounding the image
        contours, _ = cv.findContours(thresholded_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        arr = []
        for contour in contours:
            # Create a mask for the contour
            mask = np.zeros(converted_image.shape[:2], dtype=np.uint8)
            cv.drawContours(mask, [contour], -1, 255, thickness=cv.FILLED)
            
            # Dilate the contour mask into the surrounding pixels in order to get the colour
            dilated_mask = cv.dilate(mask, np.ones((5, 5), np.uint8))
            
            # Subtract the original mask to get only the surrounding pixels
            surrounding_mask = cv.subtract(dilated_mask, mask)
            
            # Get the mean color in the surrounding area
            mean_color = cv.mean(converted_image, mask=surrounding_mask)
            arr.append(mean_color[:3])
        
        return arr

    # use arithmetic to find total pointers in respective colour
    def calculate_numbers(self, red_arr, blue_arr):
        red_in_brown = 0
        red_in_green = 0
        blue_in_green = 0
        blue_in_brown = 0

        for a in red_arr:
            if a[2] != 0:                  #the red value in bgr when pointer is in brown is 0
                red_in_brown+=1     
            else:
                red_in_green+=1
        for a in blue_arr:                  
            if a[2]!=0:        
                blue_in_brown+=1
            else:
                blue_in_green+=1

        return (red_in_brown, red_in_green, blue_in_brown, blue_in_green)
