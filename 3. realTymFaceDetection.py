import cv2

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier(r'AI\3.FacialRecognizer\haarcascade_frontalface_default.xml')

# Open a connection to the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Real-time Facial Recognition', frame)

    # Break the loop and close the application if the user clicks the close button (cross symbol)
    key = cv2.waitKey(1)
    if key and cv2.getWindowProperty('Real-time Facial Recognition', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
