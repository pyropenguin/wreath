'''
Simple image capture script
'''
import cv2
import time

def single_image(cap):
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

def multiple_images(cap, num_images=10):
    for i in range(num_images):
        # Capture an image
        ret, frame = cap.read()
        if ret:
            print('ret:', ret)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

            # cv2.imshow('frame', rgb)
            # cv2.waitKey(0)

            # Save image to jpeg
            cv2.imwrite('image{}.jpg'.format(i), rgb)
            time.sleep(0.1)
        else:
            print('No image captured')

if __name__ == '__main__':
    # Create a new ImageCapture object
    cap = cv2.VideoCapture(0)

    # # Capture a single image
    # single_image(cap)

    # Capture multiple images
    multiple_images(cap, 100)

    cap.release()
    cv2.destroyAllWindows()

