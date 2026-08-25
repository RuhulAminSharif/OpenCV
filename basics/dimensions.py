import cv2

image = cv2.imread("images/image.png")
if image is not None:
    print("Image loaded successfully")
    # (height, width, channel)
    h, w, c = image.shape
    print(image.shape)
    print(f"Image Height: {h}\nWidth: {w}\nColor Channles: {c}")
else:
    print("Error: Image not found")
