#!/usr/local/bin/python
# Notes: 
#
# Original
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
# Black background - works
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=50,minRadius=0,maxRadius=0)
# Perfect mostly
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=20,minRadius=20,maxRadius=40)

import cv2
import numpy as np

# Detect pupil from eye image and outline the pupil/pupil center
def drawPupilCenter(file):
    # Read in a eye image file
    img = cv2.imread(file,0)
    # Blur the image to specified degree
    img = cv2.medianBlur(img,11)
    # Convert the image to greyscale
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    # Detect circles in image using opencv HOUGH_GRADIENT, which finds circles in a grayscale image using Hough transform
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=45,param2=20,minRadius=20,maxRadius=40)

    # Draw detected circles in greyscale converted image
    if circles is None:
        print("No circles found in " + file)
        circles = np.uint16()  # remove?
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # Draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # Draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            break  # Only draw the first detected circle, tends to be the right one

    # Show the modified image in popup window
    cv2.imshow('detected circles',cimg)
    # Save pupil detected image
    cv2.imwrite("annotated_%s.png"%file[:-4], cimg)  # [:-4] = exclude '.jpg'
    # Keep window open until any key press
    cv2.waitKey(0)  
    # Close window after key press
    cv2.destroyAllWindows()  

drawPupilCenter('37.jpg')
drawPupilCenter('9.jpg')
drawPupilCenter('14.jpg')
drawPupilCenter('23.jpg')
drawPupilCenter('29.jpg')
drawPupilCenter('ww.jpg')
drawPupilCenter('ww2.jpg')