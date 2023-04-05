import cv2
from pyzbar.pyzbar import decode
# Initialize the camera
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("http://192.168.43.113:4747/video")
# Loop over frames from the camera
while True:
    
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Decode any barcode(s) in the frame
    barcodes = decode(frame)
    
    # Draw a rectangle around each barcode and display the decoded data and barcode type
    for barcode in barcodes:
        # Extract the barcode location and draw a rectangle around it
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Print the decoded data and barcode type
        print(f'Data: {barcode.data.decode("utf-8")}, Type: {barcode.type}')
    
    # Display the frame
    cv2.imshow('Barcode Scanner', frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
