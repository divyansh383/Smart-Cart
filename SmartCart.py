import requests
print("SMART CART");
while(True):
    print("Read the barcode !");
    barcode_data=str(input());
    print("Barcode data : ",barcode_data);
    response=requests.post('http://localhost:8000/getBarcode',{'productID':barcode_data});
    if(response.status_code==200):
        print("Added to Cart")
    else:
        print("Error : ",str(response.status_code))
    print()
    