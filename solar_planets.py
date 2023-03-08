import cv2

img = cv2.imread("PRO-104-Project-Image-main/solar-system.jpg")

 #  the putText() method to add text over the image. 
cv2.putText(img,  
           "Sun",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=1,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mercury",
           (115, 190),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Venus",
           (190, 255),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (285,160),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "<-- Moon",
           (345, 175),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.3,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (385, 255),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (580, 50),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (750, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (965, 130),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1110, 290),   
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Planets In Our Solar System",
           (350, 400),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX,
           fontScale=1,  
           color=(150,200,0)
           )
cv2.imshow("output",img)
cv2.waitKey(0)
