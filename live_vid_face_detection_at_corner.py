# -*- coding: utf-8 -*-
"""live_vid_face_detection_at_corner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ku0_WvhFvh-SSxKY2hu6nf3i5hfSfPd2
"""

import cv2

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)  # Use 0 for the default webcam

while True:
    # Read a frame from the video stream
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Crop the face region
        face_roi = frame[y:y+h, x:x+w]

        # Resize the face region to a smaller size
        face_resized = cv2.resize(face_roi, (100, 100))

        # Display the resized face on the top corner of the screen
        frame[0:100, 0:100] = face_resized

    # Display the frame with the face on the top corner
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()