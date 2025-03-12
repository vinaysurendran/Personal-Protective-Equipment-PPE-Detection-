from ultralytics import YOLO
import os
import cv2
import math

cap = cv2.VideoCapture(0) # Webcam
#cap.set(3,430)
#cap.set(4,640)
cap.set(3, 1280)
cap.set(4, 720)

#cap = cv2.VideoCapture("")  # For Video
modelpath = r"C:\Users\vinay\Code\Python files\ppe\ppe.pt"
model = YOLO(modelpath)
 
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']
myColor = (0, 0, 255)
while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            w, h = x2 - x1, y2 - y1
           
 
            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            print(currentClass)
            if conf>0.5:
                if currentClass =='NO-Hardhat' or currentClass =='NO-Safety Vest' or currentClass == "NO-Mask":
                    myColor = (0, 0,255)
                elif currentClass =='Hardhat' or currentClass =='Safety Vest' or currentClass == "Mask":
                    myColor =(0,255,0)
                else:
                    myColor = (255, 0, 0)
                label = f'{classNames[int(cls)]} {conf}'
                cv2.putText(img, label, (x1, y1 - 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)
 
    cv2.imshow("PPE Detection",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
            break