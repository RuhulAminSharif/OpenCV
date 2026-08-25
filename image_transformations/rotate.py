import cv2

image = cv2.imread("images/image.png")

if image is not None:
    # Rotate 90 degrees clockwise
    rotated_90_cw = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Rotate 90 degrees counter-clockwise
    rotated_90_ccw = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Rotate 180 degrees
    rotated_180 = cv2.rotate(image, cv2.ROTATE_180)
    
    # Arbitrary Angle Rotation
    height, width = image.shape[:2]

    # Define rotation center (image center)
    center = (width // 2, height // 2)
    
    # rotation angle in degrees (positive = counter-clockwise)
    angle = 45 
    
    # scale factor (1.0 = no scaling)
    scale = 1.0 
    
    # build rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    rotated = cv2.warpAffine(src=image, M=rotation_matrix, dsize=(width, height))
    

    cv2.imshow("Original", image)
    cv2.imshow("90° CW", rotated_90_cw)
    cv2.imshow("90° CCW", rotated_90_ccw)
    cv2.imshow("180°", rotated_180)
    cv2.imshow(f"Rotated {angle}", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
