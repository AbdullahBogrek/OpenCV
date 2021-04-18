import cv2
import numpy
import matplotlib

def resizewithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):

    dim = None
    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img
    
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)

    else: 
        r = width / float(h)
        dim = (width, int(h*r))

    return cv2.resize(img, dim, interpolation = inter)

img = cv2.imread("palm.jpg")
img1 = resizewithAspectRatio(img, width = None, height = 600, inter = cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()