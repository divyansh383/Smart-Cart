import cv2
from pyzbar.pyzbar import decode
import requests
#cap = cv2.VideoCapture(0)
cap=cv2.VideoCapture("http://<IPaddress:portnumber>/video")

while(True):
    ret,frame=cap.read()
    barcodes=decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data=barcode.data.decode("utf-8");
        print("data :",barcode_data);
        response=requests.post('http://<ipaddress>:8000/getBarcode',{'productID':str(barcode_data)});
        if(response.status_code==200):
            print("Recieved at backend")
        else:
            print("Error : ",str(response.status_code))
        print("----------------")
        
    cv2.imshow('Barcode Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
