import cv2
from pyzbar.pyzbar import decode
import requests
import json
import requests
import datetime 

# Make one method to decode the barcode
def BarcodeReader(image):
	
	# read the image in numpy array using cv2
	# img = cv2.imread(image)
	
	# Decode the barcode image
    detectedBarcodes = decode(image)
	
	# If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
	
		# Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
		
			# Locate the barcode position in image
            (x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to heighlight the barcode
			# cv2.rectangle(img, (x-10, y-10),
			# 			(x + w+10, y + h+10),
			# 			(255, 0, 0), 2)
			
            if barcode.data!="":
                return barcode.data


def barcode_scanner():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    cv2.namedWindow('Barcode Scanner')





    count = 0
    while(True):
        _,frame = cap.read()

        
        cv2.imshow('test', frame)
        waiting = cv2.waitKey(1)
        barcode_num = BarcodeReader(frame)
        if(barcode_num):
            print(barcode_num.decode("utf-8")[1:])
            return (barcode_num.decode("utf-8")[1:] )
            
    

def api_grab (barcode):
    product_info = requests.get("https://world.openfoodfacts.org/api/v0/product/"+barcode+".json")
    
    response_dict = json.loads(product_info.text)

    for key, value in response_dict.items():
        if key == "product":
            for key1, value1 in value.items():
                if key1 == "serving_quantity":
                    serving_amount = value1
                elif key1 == "quantity":
                    total_amount = value1

    return [serving_amount,total_amount]


print(api_grab(barcode_scanner()))





