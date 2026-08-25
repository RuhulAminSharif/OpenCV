import cv2

image = cv2.imread("images/image.png")

if image is None:
    print("Error: Image not found")
else:
    height, width = image.shape[:2]

    # resize to specific dimensions
    resized = cv2.resize(src=image, dsize=(600, 300))  # (300, 600) ==> (width, height)

    cv2.imwrite("images/resized.png", resized)

    # resize by scaling factor
    scaled = cv2.resize(
        src=image, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR
    )
    cv2.imwrite("images/scaled.png", scaled)

    # resize maintainig aspect ratio
    new_width = 400
    aspect_ratio = new_width / width
    new_height = int(height * aspect_ratio)
    resized_aspect = cv2.resize(
        src=image, 
        dsize=(new_width, new_height)
    )
    cv2.imwrite("images/resized_aspect.png", resized_aspect)

    cv2.imshow("Original", image)
    cv2.imshow("Resized", resized)
    cv2.imshow("Scaled", scaled)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
