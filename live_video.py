'''
Simple video play script
'''
import cv2

# Create a new ImageCapture object
cap = cv2.VideoCapture(0)

# Capture an image
while True:
    ret, frame = cap.read()
    if ret:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        cv2.waitKey(1)
    else:
        print('No image captured')
        break

cap.release()
cv2.destroyAllWindows()
