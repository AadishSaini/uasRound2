## UAS DTU Round 2 task

 The folders in the repository are:-

 - logbook:- contains the work i did on a specific date
 - solution:- contains the code for the task given
 - practise-code:- the code i wrote while learning the libraries

How i approached the task, 

 1. Read the image.<br/>                                                   ![original image](./solution/images/1.png)<br/>  <br/>  
 2. Converted the image to hsv.<br/>                       ![enter image description here](./readme_images/hsv.png)<br/>  <br/>  
 3. Created different masks for different colours.<br/>![pointer masks s white](./readme_images/pointers_mask_white.png)![green brown mask white](./readme_images/green_brown_mask_white.png)<br/>  <br/>  
 4. Used blue colour overlay to depict green part, and yellow colour overlay to depict brown part. <br/>                               ![pointers masks](./readme_images/pointers_mask.png)![area masks](./readme_images/green_brown_mask.png)<br/>  <br/>  
 5. Next, i used contours to identify the pointers in masked images.<br/>![contour](./readme_images/contours.png)<br/>  <br/>  
6. Now i found the surrounding colours using the dilute function of cv and found the mean of the values.<br/>
7. Then i compared the values of these surrounding pixels and updated the different numbers.<br/>