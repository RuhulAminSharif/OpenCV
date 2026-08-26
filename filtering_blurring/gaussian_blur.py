import cv2

image = cv2.imread("images/nature.png")

if image is not None:
    blurred = cv2.GaussianBlur(src=image, ksize=(7, 7), sigmaX=0)
    
    cv2.imshow("Original", image)
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
