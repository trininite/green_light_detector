import cv2
import os

def cam_init_wizard() -> cv2.VideoCapture:
    """
    A wizard for selecting the right camera

    Goes through cam 0-9, selects it and asks if the webcam light is on to 
    determine if the correct camera is selected.

    Returns:
        cv2.VideoCapture: A VideoCapture object associated with the selected
            camera device.
    """
    for i in range(10):
        camera = cv2.VideoCapture(i)
        print("Check for webcam light, correct device?")
        correct = input("(Y/n)")
        if correct == "N" or correct == "n":
            camera.release()
            continue
        else:
            print(f"Selecting camera index: {i}")
            break

    if not camera.isOpened():
        raise Exception("could not open camera")

    print("taking testing frame")
    ret, test_frame = camera.read()
    if not ret:
        print("failed to grab frame, exiting...")
        exit()
    cv2.imwrite("TEST.jpg", test_frame)
    delete = input("is image good (Y/N)")
    os.remove("TEST.jpg")
    if delete == "N" or delete == "n":
        print("bad image, quitting...")
        quit()

    return camera