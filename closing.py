import erosion
import dilation
import cv2
import sys


# closing is the erosion of the dilation of an image.
def closing(img, out):
    # dilate image
    dilated = dilation.dilation(img, out)
    # erode dilated image
    closed = erosion.erosion(dilated, out)
    # write result to file
    cv2.imwrite(out, closed)

if __name__ == '__main__':
    image_path = sys.argv[1]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    closing(image, sys.argv[2])

