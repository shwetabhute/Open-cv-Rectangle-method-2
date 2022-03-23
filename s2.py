import cv2
path = 'numpy.jpg'
image = cv2.imread(path)
window_name = 'Image'
start_point = (80, 60)
end_point = (200, 100)
color = (0, 0, 0)
thickness = -2
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
