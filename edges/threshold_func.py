import cv2

image = cv2.imread("images/nature.png", cv2.IMREAD_GRAYSCALE)

if image is not None:
    ret, thresh_img = cv2.threshold(
        src=image, thresh=120, maxval=255, type=cv2.THRESH_BINARY
    )

    cv2.imshow("Original", image)
    cv2.imshow("Threshold", thresh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
