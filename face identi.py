import cv2

trainedDataset= cv2.CascadeClassifier( "misc.xml")

img=cv2.imread('image/iyyappa.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=trainedDataset.detectMultiScale(img)
print(face)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow('gray',gray)
cv2.imshow('im',img)
cv2.waitKey()