import cv2

image = cv2.imread("images/nature.png", cv2.IMREAD_GRAYSCALE)

if image is not None:
    edges = cv2.Canny(image=image, threshold1=50, threshold2=150)

    cv2.imshow("Original", image)
    cv2.imshow("Canny Edge", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
