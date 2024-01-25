import cv2

# Step 4: Load the cascade classifier
face_cascade = cv2.CascadeClassifier(r'AI\4.catFaceRecognizer.py\haarcascade_frontalcatface.xml')
# Replace 'path_to_haarcascade_frontalface_default.xml' with the actual path to the downloaded XML file.

# Step 5: Read the image
image_path1 = r'AI\4.catFaceRecognizer\test_cat1.jpg'
image_path2 = r'AI\4.catFaceRecognizer\test_cat2.jpg'
image_path3 = r'AI\4.catFaceRecognizer\test_cat3.jpg'
img = cv2.imread(image_path1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 6: Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

# Step 7: Draw rectangles around the faces
cnt=0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(img, f"{cnt}", (x+5,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.9, (150,200,250), 2)
    cnt+=1

# Step 8: Display the result
cv2.imshow('Facial Recognition', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
