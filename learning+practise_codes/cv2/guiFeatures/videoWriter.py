import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'DVIX')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()

    if not ret:
        print('cant read frame')
        break

    out.write(frame)

    cv.imshow('window', frame)
    if cv.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv.destroyAllWindows()