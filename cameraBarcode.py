import pyzbar.pyzbar as pyzbar
import cv2
import requests
def scan():
    i=0
    cap=cv2.VideoCapture(0)
    while(i<1):
        _,frame=cap.read()
        decoded=pyzbar.decode(frame)
        for obj in decoded:
            print("data:",obj.data)
            response=requests.post('http://localhost:8000/getBarcode',{'productID':str(obj.data)});
            if(response.status_code==200):
                print("Recieved at backend")
            else:
                print("Error : ",str(response.status_code))
            print("----------------")
            i+=1
        cv2.imshow("qr",frame)
        cv2.waitKey(5)
        cv2.destroyAllWindows

scan()

#respberry pi
# import pyzbar.pyzbar as pyzbar
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import time

# def scan():
#     i=0
#     camera = PiCamera()
#     camera.resolution = (640, 480)
#     rawCapture = PiRGBArray(camera, size=(640, 480))
#     time.sleep(0.1) # Allow camera to warm up
#     for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#         image = frame.array
#         decoded=pyzbar.decode(image)
#         for obj in decoded:
#             print("data:",obj.data)
#             i+=1
#         cv2.imshow("qr",image)
#         key = cv2.waitKey(1) & 0xFF
#         rawCapture.truncate(0)
#         if i>=4:
#             break
            
#     cv2.destroyAllWindows()

# scan()
