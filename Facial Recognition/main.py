import cv2

camera = cv2.VideoCapture(0)

face_casc = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_casc = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

while True:
    _, frame = camera.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_casc.detectMultiScale(grey, 1.3, 5)

    for (x, y, width, height) in faces:
       cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
