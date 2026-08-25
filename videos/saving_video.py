import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*"XVID")  # type: ignore
recorder = cv2.VideoWriter(
    filename="video.avi", fourcc=codec, fps=20, frameSize=(frame_width, frame_height)
)

while True:
    success, image = camera.read()
    
    if not success:
        break
    
    recorder.write(image)
    cv2.imshow("Recording live", image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
camera.release()
recorder.release()
cv2.destroyAllWindows()