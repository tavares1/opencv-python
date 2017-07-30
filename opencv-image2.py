import numpy as np
import cv2 

img = cv2.imread("images.jpeg",0)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("babygray.png",img)
    cv2.destroyAllWindows()
    
