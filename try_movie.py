import cv2
data = cv2.VideoCapture('./sample.mp4')
delay = 1
while True:
    ret, frame = data.read()
    if ret:
        cv2.imshow('sample data', frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)
cv2.destroyWindow('sample data')