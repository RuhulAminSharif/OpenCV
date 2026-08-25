import cv2
import numpy as np

# white image
image = np.full((500, 500, 3), 255, dtype=np.uint8)

if image is not None:
    print("Image loaded")

    pt = (50, 100)  # bottom-left corner

    color = (0, 0, 255)

    cv2.putText(
        img=image,
        text="hello",
        org=pt,
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.0,
        color=color,
        thickness=4,
    )

    cv2.imshow("Window Title", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
