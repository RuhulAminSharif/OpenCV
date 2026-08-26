import cv2

face_cascade = cv2.CascadeClassifier(
    "face_object_detection/haarcascades/haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    "face_object_detection/haarcascades/haarcascade_eye.xml"
)
smile_cascade = cv2.CascadeClassifier(
    "face_object_detection/haarcascades/haarcascade_smile.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        cv2.rectangle(
            img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2
        )

        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

        eyes = eye_cascade.detectMultiScale(
            image=roi_gray, scaleFactor=1.01, minNeighbors=5
        )
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
            cv2.putText(
                frame,
                "Eyes Open",
                (x, y - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2,
            )

        smiles = smile_cascade.detectMultiScale(
            image=roi_gray, scaleFactor=1.1, minNeighbors=15
        )
        for sx, sy, sw, sh in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
            cv2.putText(
                frame,
                "Smiling!",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )

    cv2.imshow("Webcam Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
