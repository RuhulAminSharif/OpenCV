import cv2

image = cv2.imread("images/image.png")
if image is not None:
    print("Image loaded successfully")
    success = cv2.imwrite("images/output.png", image)
    if success:
        print("Image save successfully as 'output.png'")
    else:
        print("Failed to save an image")
else:
    print("Error: Image not found")
