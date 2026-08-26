import cv2
import numpy as np

image = cv2.imread("images/hand.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.erode(thresh, kernel, iterations=2)
    thresh = cv2.dilate(thresh, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    cv2.drawContours(
        image=image, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3
    )

    # 6. Display the result
    cv2.imshow("Contours", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
