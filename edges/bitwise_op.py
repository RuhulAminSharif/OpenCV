import cv2
import numpy as np

# two black canvas images (300x300 pixels)
canvas_rect = np.zeros((300, 300), dtype="uint8")
canvas_circle = np.zeros((300, 300), dtype="uint8")

# a white rectangle and a white circle
cv2.rectangle(canvas_rect, (25, 25), (275, 275), 255, -1)
cv2.circle(canvas_circle, (150, 150), 150, 255, -1)

bit_and = cv2.bitwise_and(canvas_rect, canvas_circle)  # Intersection
bit_or = cv2.bitwise_or(canvas_rect, canvas_circle)  # Union
bit_xor = cv2.bitwise_xor(canvas_rect, canvas_circle)  # Non-overlapping parts
bit_not = cv2.bitwise_not(canvas_rect)  # Inversion

cv2.imshow("AND (Intersection)", bit_and)
cv2.imshow("OR (Union)", bit_or)
cv2.imshow("XOR", bit_xor)
cv2.imshow("NOT Rectangle", bit_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
