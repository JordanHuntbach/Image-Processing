import erosion
import dilation
import cv2
import sys


# opening is the dilation of the erosion of an image.
def opening(img, out):
    # erode image
    eroded = erosion.erosion(img, out)
    # dilate eroded image
    opened = dilation.dilation(eroded, out)
    # write result to file
    cv2.imwrite(out, opened)

if __name__ == '__main__':
    image_path = sys.argv[1]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    opening(image, sys.argv[2])

