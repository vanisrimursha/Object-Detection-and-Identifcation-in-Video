
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 21:57:14 2019

@author: DELL
"""

import cv2
#import numpy as np
 
cap = cv2.VideoCapture("E:\\VANISRI-MCA\\SET5001\\Datasets\\Video Datas\\highway.mp4")
 
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
 
while True:
    _, frame = cap.read()
 
    mask = subtractor.apply(frame)
 
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()