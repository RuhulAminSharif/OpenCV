import cv2
import numpy as np

# white image
image = np.full((500, 500, 3), 255, dtype=np.uint8)

if image is not None:
    print("Image loaded")

    center = (150, 160)
    radius = 80

    color = (0, 0, 255)
    thickness = -1  # positive for outlined box, -1 or cv2.FILLED to crate a solid/filled rectangle

    cv2.circle(img=image, center=center, radius=radius, color=color, thickness=thickness)

    cv2.imshow("Window Title", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
