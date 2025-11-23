import cv2

trainedDataset= cv2.CascadeClassifier( "misc.xml")

vedios = cv2.VideoCapture(0)

while True:
            success, frame = vedios.read()
            if success == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                face = trainedDataset.detectMultiScale(gray)
                for (x, y, w, h) in face:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow('frame',frame)
                key=cv2.waitKey(1)
                if key ==81 or key == 113:
                    break
            else:
                print("vedio end")
                break