'''
Simple image capture script
'''
import cv2

# Create a new ImageCapture object
cap = cv2.VideoCapture(0)

# Capture an image
ret, frame = cap.read()
if ret:
    print('ret:', ret)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # cv2.imshow('frame', rgb)
    # cv2.waitKey(0)

    # Save image to jpeg
    cv2.imwrite('image.jpg', rgb)
else:
    print('No image captured')

cap.release()
cv2.destroyAllWindows()
