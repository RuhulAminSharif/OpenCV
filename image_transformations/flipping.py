import cv2

image = cv2.imread("images/image.png")

if image is not None:
    # Flip horizontally (mirror)
    flipped_h = cv2.flip(image, 1)

    # Flip vertically
    flipped_v = cv2.flip(image, 0)

    # Flip both horizontally and vertically
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("Horizontal Flip", flipped_h)
    cv2.imshow("Vertical Flip", flipped_v)
    cv2.imshow("Both", flipped_both)
    cv2.waitKey(0)