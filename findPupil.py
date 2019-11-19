# Detect/draw pupil and pupil center
#!/usr/local/bin/python
import cv2
import numpy as np

def drawPupilCenter(file):
    img = cv2.imread(file,0)
    img = cv2.medianBlur(img,11)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    # Original
    # circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

    # Black background - works
    # circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=50,minRadius=0,maxRadius=0)

    # Perfect mostly
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=20,minRadius=20,maxRadius=40)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=45,param2=20,minRadius=20,maxRadius=40)


    if circles is None:
        print("No circles found in " + file)
        circles = np.uint16()
    else:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            break  # Only draw the first detected circle, tends to be the right one

    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)  # Keep open until any key press
    cv2.destroyAllWindows()  # Close window after key press

drawPupilCenter('1.jpg')
drawPupilCenter('2.jpg')
drawPupilCenter('3.jpg')
drawPupilCenter('4.jpg')
drawPupilCenter('5.jpg')
drawPupilCenter('6.jpg')
drawPupilCenter('7.jpg')
drawPupilCenter('8.jpg')