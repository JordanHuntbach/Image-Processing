import cv2
import numpy
import copy
import sys


# this sets the value of each pixel to the maximum value that is within the structuring element, when centered on the
# pixel; in this case, the structuring element is a 5 pixel x 5 pixel square
def dilation(img, out):
    # get image properties
    h, w = numpy.shape(img)
    # copy image
    new = copy.copy(img)
    # iterate over pixels
    for pixel_y in range(0, w):
        for pixel_x in range(0, h):
            # extract 5x5 pixel area
            roi = img[max(0, pixel_y - 2): min(h, pixel_y + 3),
                      max(0, pixel_x - 2): min(w, pixel_x + 3)]
                      # set the centre pixel to the maximum value
            new[pixel_y][pixel_x] = numpy.amax(roi)
    # write new image to file
    cv2.imwrite(out, new)
    return new

if __name__ == '__main__':
    image_path = sys.argv[1]
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    dilation(image, sys.argv[2])

