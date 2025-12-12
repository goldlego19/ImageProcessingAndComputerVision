# import the necessary packages


import cv2
import numpy as np

def donothing(x):
    pass

img = cv2.imread('./images/lena.jpg')
im_mod = img.copy()


cv2.namedWindow("Task 2")
#label of trackbar, window title, starting value, ending value, method that is called on change
cv2.createTrackbar('CropX', 'Task 2', 1, int(img.shape[0]/2-10), donothing)
cv2.createTrackbar('CropY', 'Task 2', 1, int(img.shape[1]/2-10), donothing)
cv2.createTrackbar('CropX2','Task 2', 1, int(img.shape[0]/2-10), donothing)
cv2.createTrackbar('CropY2','Task 2', 1, int(img.shape[1]/2-10), donothing)


while True:

    cropLeft = cv2.getTrackbarPos("CropX", "Task 2")
    cropUp = cv2.getTrackbarPos("CropY", "Task 2")
    cropRight = cv2.getTrackbarPos("CropX2", "Task 2")
    cropDown = cv2.getTrackbarPos("CropY2", "Task 2")

    if cropLeft <= 1:
        cropLeft = 1
    if cropUp <= 1:
        cropUp = 1
    if cropRight <= 1:
        cropRight = 1
    if cropDown <= 1:
        cropDown = 1
    

    im_mod = img[cropUp:-cropDown,cropLeft:-cropRight,:]
    print(im_mod.shape)


    cv2.imshow("Output ", im_mod)


    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break
