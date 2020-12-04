import cv2

def takeSnapshot():
    videocaptureobject= cv2.VideoCapture(0)
    result= True
    while(result):
        ret, frame = videocaptureobject.read()
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows()

takeSnapshot()