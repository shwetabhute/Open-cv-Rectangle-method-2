# importing cv2 
import cv2
# path 
path = 'numpy.jpg'
# Reading an image in default mode
image = cv2.imread(path)
# Window name in which image is displayed
window_name = 'Image'
# Start coordinate, here ((80, 60)
# represents the top left corner of rectangle
start_point = (80, 60)
# Ending coordinate, here (200, 100)
# represents the bottom right corner of rectangle
end_point = (200, 100)
# Black color in BGR
color = (0, 0, 0)
# Line thickness of -2 px
# Thickness of -2 will fill the entire shape
thickness = -2
# Using cv2.rectangle() method
# Draw a rectangle of black color of thickness -1 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
# Displaying the image 
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
