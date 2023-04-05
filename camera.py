import cv2
from pyzbar.pyzbar import decode

# Initialize the camera module
cap = cv2.VideoCapture(0)

# Continuously capture and process images
while True:
    ret, frame = cap.read()
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        print(obj.data)

    # Display the captured frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy the window
cap.release()
cv2.destroyAllWindows()
