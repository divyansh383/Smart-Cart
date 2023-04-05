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

