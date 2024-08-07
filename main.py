import cv2

# Configuration Parameters
source = "image.jpeg"
destination = 'newImage.jpeg'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
