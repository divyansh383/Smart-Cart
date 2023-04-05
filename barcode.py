import RPi.GPIO as GPIO
import time
import cv2
from pyzbar.pyzbar import decode
import requests

# Setup GPIO pins for LEDs------------------------
green_pin = 17
red_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
#----------------------------------------------
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("http://172.16.6.232:4747/video")

while True:
    ret, frame = cap.read()
    barcodes = decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data = barcode.data.decode("utf-8")
        print("data:", barcode_data)
        response = requests.post('http://172.16.6.150:8000/getBarcode', {'productID': str(barcode_data)})
        if response.status_code == 200:
            # Blink green LED
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(green_pin, GPIO.LOW)
            print("Received at backend")
        else:
            # Blink red LED
            GPIO.output(red_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(red_pin, GPIO.LOW)
            print("Error:", str(response.status_code))
        print("----------------")

    cv2.imshow('Barcode Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up GPIO pins
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
