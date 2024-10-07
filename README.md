## UAS DTU Round 2 task

How i approached the task, 

 1. Read the image.                                                     ![original image](./solution/images/1.png)
 2. Converted the image to hsv.                       ![enter image description here](./readme_images/hsv.png)
 3. Created different masks for different colours.![pointer masks s white](./readme_images/pointers_mask_white.png)![green brown mask white](./readme_images/green_brown_mask_white.png)
 4. Used blue colour overlay to depict green part, and yellow colour overlay to depict brown part.                                ![pointers masks](./readme_images/pointers_mask.png)![area masks](./readme_images/green_brown_mask.png)
 5. Next, i used contours to identify the pointers in masked images.![contour](./readme_images/contours.png)
6. Now i found the surrounding colours using the dilute function of cv and found the mean of the values.
7. Then i compared the values of these surrounding pixels and updated the different numbers.