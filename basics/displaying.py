import cv2

image = cv2.imread("images/image.png")
if image is not None:
    print("Image loaded successfully")
    # diplay using imshow
    cv2.imshow("Window Title", image) # open the window
    cv2.waitKey(0) # wait for a key
    cv2.destroyAllWindows() # close the window
else:
    print("Error: Image not found")

