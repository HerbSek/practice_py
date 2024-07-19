# import cv2
# import numpy as np 

# cam = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# if not cam.isOpened():
#     raise IOError('Cannot find camera !!!')
# try:
#     while True:
#         ret, frame = cam.read()
#         frame = cv2.flip(frame,1)

#         if not ret:
#             break
#         get_face = face_cascade.detectMultiScale(frame, 1.1, 5)
#         for (x,y,i,j) in get_face:
#             cv2.rectangle(frame, (x,y), (x+i, y+j), (255,0,0), 1)
#             print(f' x= {x} and y={y}')

#         cv2.imshow('frame', frame)

#         c = cv2.waitKey(11)
#         if c == 27:
#             break
# except Exception as e:
#     print(f' error : {e}')
        
# cam.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np

# Load the pre-trained face cascade classifier from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# Load the face mask image
face_mask = cv2.imread('hannibal.jpg')
h_mask, w_mask = face_mask.shape[:2]

# Check if the face cascade classifier has been loaded correctly
if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)
# scaling_factor = 0.5

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    # Resize the frame to the specified scaling factor
    frame = cv2.resize(frame, (600,500), interpolation=cv2.INTER_AREA)
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    face_rects = face_cascade.detectMultiScale(gray, 1.2, 6)
    
    for (x, y, w, h) in face_rects:
        if h > 0 and w > 0:
            # Adjust the size and position of the detected face region
            h, w = int(1.4 * h), int(1.0 * w)
            y = int(y - 0.1 * h)
            
            # Extract the region of interest (ROI) from the frame
            frame_roi = frame[y:y+h, x:x+w]
            
            # Resize the face mask to fit the detected face region
            face_mask_small = cv2.resize(face_mask, (w, h), interpolation=cv2.INTER_AREA)
            
            # Convert the face mask to grayscale and threshold it to create a mask
            gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_mask, 180, 255, cv2.THRESH_BINARY_INV)
            
            # Create an inverse mask
            mask_inv = cv2.bitwise_not(mask)
            
            # Use the mask to extract the face mask region of interest
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
            
            # Use the inverse mask to get the remaining part of the frame ROI
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            
            # Add the two images to get the final output
            frame[y:y+h, x:x+w] = cv2.add(masked_face, masked_frame)
    
    # Display the resulting frame
    cv2.imshow('Face Detector', frame)
    
    # Break the loop if 'Esc' key is pressed
    c = cv2.waitKey(1)
    if c == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
