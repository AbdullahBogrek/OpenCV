import cv2

def camera():
        
    while True:
        
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

def record():
    filename = "/home/abdullah/Desktop/OpenCV/webcam.mp4"
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    frameRate = 30
    resolution = (640,480)

    videoFileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        videoFileOutput.write(frame)

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    videoFileOutput.release()

cap = cv2.VideoCapture(0)

record()

cap.release()
cv2.destroyAllWindows()