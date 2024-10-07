import cv2 as cv
import numpy as np
from consts import *



def create_mask(image, LOWER, UPPER):
    lower = np.array(LOWER)
    upper = np.array(UPPER)
    mask = cv.inRange(image, lower, upper)
    return mask

def return_contours(masked_image, to_mask_on):
    gray_image = cv.cvtColor(masked_image, cv.COLOR_BGR2GRAY)
    _, thresholded_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(thresholded_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_image = cv.drawContours(to_mask_on.copy(), contours, -1, (0, 255, 0), 2)
    return contour_image, contours

def surrounding_colours(contours, image):
    arr = []
    for contour in contours:
        # Create a mask for the contour
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv.drawContours(mask, [contour], -1, 255, thickness=cv.FILLED)
        
        # Dilate the contour mask to get surrounding pixels
        dilated_mask = cv.dilate(mask, np.ones((5, 5), np.uint8))
        
        # Subtract the original mask to get only the surrounding pixels
        surrounding_mask = cv.subtract(dilated_mask, mask)
        
        # Get the mean color in the surrounding area
        mean_color = cv.mean(image, mask=surrounding_mask)
        arr.append(mean_color[:3])
    
    return arr

#create a blank blue and yellow screen
blue_screen = np.full((640, 640, 3), (255, 255, 0), dtype=np.uint8)
yellow_screen = np.full((640, 640, 3), (0, 255, 255), dtype=np.uint8)


for ai in range(1, 12):
    if ai == 9:
        continue

    #declare variables
    red_in_green = 0
    red_in_brown = 0
    blue_in_green = 0
    blue_in_brown = 0

    image = cv.imread('./images/'+str(ai)+'.png')

    #convert image to hsv
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)



    #create mask for each colour
    green_mask = create_mask(hsv_image, GREEN_LOWER_HSV, GREEN_UPPER_HSV)
    brown_mask = create_mask(hsv_image, BROWN_LOWER_HSV, BROWN_UPPER_HSV)
    red_mask = create_mask(hsv_image, RED_POINTER_LOWER_HSV, RED_POINTER_UPPER_HSV)
    blue_mask = create_mask(hsv_image, BLUE_POINTER_LOWER_HSV, BLUE_POINTER_UPPER_HSV)


    #apply the masks on original image
    result_green_mask = cv.bitwise_and(blue_screen, blue_screen, mask=green_mask)
    result_brown_mask = cv.bitwise_and(yellow_screen, yellow_screen, mask=brown_mask)
    result_red_mask = cv.bitwise_and(image, image, mask=red_mask)
    result_blue_mask = cv.bitwise_and(image, image, mask=blue_mask)


    #add the masked images
    result1 = cv.addWeighted(result_green_mask, 1, result_red_mask, 1, 0)
    result2 = cv.addWeighted(result_brown_mask, 1, result1, 1, 0)
    result = cv.addWeighted(result_blue_mask, 1, result2, 1, 0)


    # contours
    red_pointer_contour, c_r = return_contours(result_red_mask, result)
    blue_pointer_contour, c_b = return_contours(result_blue_mask, result)

    #get surrounding colours for red
    red_arr = surrounding_colours(c_r, result)
    blue_arr = surrounding_colours(c_b, result)
    
    for a in red_arr:
        if a[2] != 0:
            red_in_brown+=1
        else:
            red_in_green+=1
    for a in blue_arr:
        if a[2]!=0:
            blue_in_brown+=1
        else:
            blue_in_green+=1

    cv.imshow('APPLIED ALL', image)

    
    print("\n\n\n")
    print("image: ", ai)
    print("red in brown = ",red_in_brown)
    print("red in green = ", red_in_green)
    print("blue in brown = ", blue_in_brown)
    print("blue in green", blue_in_green)
    print("\n\n\n")

    #end
    cv.waitKey(0)
    cv.destroyAllWindows()

