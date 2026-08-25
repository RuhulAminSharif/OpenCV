import cv2
import numpy as np

# white image
image = np.full((500, 500, 3), 255, dtype=np.uint8)

if image is not None:
    print("Image loaded")
    
    pt1 = (50, 100)  # top-left corner
    pt2 = (300, 150)  # bottom-right corner
    
    color = (0, 0, 255)
    thickness = 1 # positive for outlined box, -1 or cv2.FILLED to crate a solid/filled rectangle
    
    cv2.rectangle(img=image, pt1=pt1, pt2=pt2, color=color, thickness=thickness)
    
    cv2.imshow("Window Title", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
