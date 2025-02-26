import cv2

def click_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "I am Sorry, there is some Problem in Capturing the Image"

    ret, frame = cap.read()

    if ret:
        cv2.imwrite('captured_photo.jpg', frame)
        return "Photo captured and saved as 'captured_photo.jpg'."
    else:
        return "I am Sorry, there is some Problem in Capturing the Image"

    cap.release()
    cv2.destroyAllWindows()

    return True
