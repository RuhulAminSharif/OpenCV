import cv2

image = cv2.imread("images/image.png")

# Define crop region (y1:y2, x1:x2)
y1, y2 = 100, 400 # for cropping along the height
x1, x2 = 300, 600 # for cropping along the width

if image is not None:
    # Crop the image
    cropped = image[y1:y2, x1:x2]
    
    cv2.imwrite("images/cropped.png", cropped)

    cv2.imshow("Original", image)
    cv2.imshow("Cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found")
