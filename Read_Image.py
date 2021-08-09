import cv2
import numpy

img = cv2.imread("redhood.jpg")

#cv2.imshow("output", img)
cv2.waitKey(0)

blue, green, red = cv2.split(img)
print(blue)
print(green)
print(red)


numpydata = numpy.array(img)
print(numpydata)

#Creating a image using numpy
zeros = numpy.zeros(blue.shape, numpy.uint8)

#cv2.imshow("black",zeros)

# blueBGR = cv2.merge((blue,zeros,zeros))
# greenBGR = cv2.merge((zeros,green,zeros))
# redBGR = cv2.merge((zeros,zeros,red))

# cv2.imshow("Blue", blueBGR)
# cv2.imshow("Green", greenBGR)
# cv2.imshow("Red", redBGR)

#Converting image to Grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("output",img)
cv2.imshow("gray",gray)

cv2.waitKey(0)
