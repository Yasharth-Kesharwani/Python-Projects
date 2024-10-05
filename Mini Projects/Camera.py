import cv2

def open_camera(quit = 'q'):
    # Open default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord(quit):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :

    open_camera()