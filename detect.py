import cv2
from gpiozero import Buzzer
from time import sleep
import time
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg['subject'] = "SURVEILLANCE ALERT"
msg['to'] = "paragg@sjcem.edu.in"
user = "abhi.parody@gmail.com"
msg['from'] = user
msg['body'] = " "
password="fcpdglsyemitbpiv"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, password)
buzzer = Buzzer(17)
#from deepface import DeepFace
# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
status=""
# Set up the video capture device (0 is the default camera)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# Define the font and color for displaying text
# Main loop
while True:
    # Capture a frame from the video
    ret, frame = cap.read()
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, status, (x-100, y-25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Display the frame
    cv2.imshow("Face Detection", frame)
    cv2.imwrite("frame.jpg", frame)
    if(type(faces)!=tuple and status!="Human presence detected!"):
        status="Human presence detected!"
        with open('frame.jpg', 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='detected_face.jpg')
        server.send_message(msg)
        while True:
            buzzer.on()
            buzzer.beep()
            break
    if(type(faces)==tuple):
        if(status=="Human presence detected!"):
            print("Detected Human moved!")
            time.sleep(1)
            with open('frame.jpg', 'rb') as f:
                img_data = f.read()
                msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='human moved.jpg')
            server.send_message(msg)
            buzzer.off()
            cv2.putText(frame, "Detected Human moved", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        status=""
    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        server.quit()
        break
# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()
