import numpy as np
import cv2

hello = cv2.imread('opencv-corner-detection-sample.jpg')
# gray = cv2.cvtColor(hello,cv2.COLOR_BGR2GRAY)
#gray = np.float64(gray)

# graycorners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# corners = np.int0(corners)
#
# for corner in corners:
#     x,y = corner.ravel()
#     cv2.circle(hello,(x,y),4,125,-2)


'''no_noise = []
for i in range(len(hello)):
    blur = cv2.GaussianBlur(hello[i], (5,5), 0)
    no_noise.append(blur)

hello = no_noise[4]
display(original, hello, 'Original', 'Blured')'''
'''no_noise = []
   for i in range(len(res_img)):
        blur = cv2.GaussianBlur(res_img[i], (5, 5), 0)
        no_noise.append(blur)

image = no_noise[4]
display(original, image, 'Original', 'Blured')'''



#cv2.imshow('Image',color)
cv2.waitKey(0)
cv2.destroyAllWindows()