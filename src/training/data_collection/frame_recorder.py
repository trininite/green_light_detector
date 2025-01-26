import cv2
import time
from datetime import datetime

# camera index (0 is usually the default camera)
camera_index = 0
# interval in seconds between captures
capture_interval = 5  
# output folder for images
output_folder = f"./captures/{datetime.now().strftime("%Y%m%d_%H%M%S")}"

# create output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# verify working dir
dir_cont = os.listdir()
if not "frame_recorder.py" in dir_cont:
    print("malformed working dir, please set absolutely")



def cam_init_wizard() -> cv2.VideoCapture:
    # initialize camera
    for i in range(10):
        camera = cv2.VideoCapture(i)
        print("Check for webcam light, correct device?")
        correct = input("(Y/N)")
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

print("Run cam wizard?")
correct = input("(Y/N) ")
if correct == "N" or correct == "n":
    cam_id = int(input("Enter camera id: "))
    camera = cv2.VideoCapture(cam_id)
else:
    print("running cam wizard")
    camera = cam_init_wizard()

itr = 0
try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("failed to grab frame")
            break
        
        # generate timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_folder, f"{itr}.jpg")
        
        # save the frame
        cv2.imwrite(filename, frame)
        print(f"saved {filename}")
        
        # wait for the next capture
        time.sleep(capture_interval)

        itr += 1

except KeyboardInterrupt:
    print("stopping capture...")

finally:
    camera.release()
    cv2.destroyAllWindows()
