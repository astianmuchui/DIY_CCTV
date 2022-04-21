import cv2
import requests
import numpy as np
import imutils

#Sample IP Adress
url = "100.120.8.107:3030/shot.jpg"

while True:
    img_rs = requests.get(url)
    
    imgs = np.array(bytearray(img_rs.content),dtype = np.uint8)
    
    img = cv2.imdecode(imgs,-1)
    
    img = imutils.resize(img,width=100,height=1200)
    
    cv2.imshow("DIY CCTV ANDROID",img)

    if cv2.waitkey(1) == 27:
        break

cv2.destroyAllWindows()
