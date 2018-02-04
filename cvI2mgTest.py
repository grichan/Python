
import numpy as np
import cv2

img = cv2.imread('startroopers.jpg',cv2.IMREAD_COLOR)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
