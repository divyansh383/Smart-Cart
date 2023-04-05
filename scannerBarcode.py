import requests
print("SMART CART")
while (True):
    print("Read the barcode !")
    barcode_data = str(input())
    print("Barcode data : ", barcode_data)
    try:
        response = requests.post(
            'http://172.16.4.189:8000/getBarcode',{'productID': barcode_data})
        if (response.status_code == 200):
            print("Added to Cart")
        else:
            print("Error : ", str(response.status_code))
    except:
        print("error")
    print()
#192.168.1.25