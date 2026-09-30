import cv2

# Face detect
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

print("Helmet Project Started - Q to Close")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        status = "HELMET DETECTED"
        bike = "BIKE: ON"
        color = (0, 255, 0)
    else:
        status = "NO HELMET"
        bike = "BIKE: OFF"
        color = (0, 0, 255)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)

    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    cv2.putText(frame, bike, (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('Smart Helmet - ECE', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
