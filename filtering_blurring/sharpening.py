import cv2
import numpy as np

image = cv2.imread("images/low_r.png")

if image is not None:
    sharpen_kernel = np.array(
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ]
    )
    sharped = cv2.filter2D(
        src=image,
        ddepth=-1,
        kernel=sharpen_kernel
    )

    cv2.imshow("Original", image)
    cv2.imshow("Sharped", sharped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
