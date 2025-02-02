import cv2
import time
import os
from datetime import datetime

from common.camera_init import cam_init_wizard


# camera index (0 is usually the default camera)
camera_index = 0
# interval in seconds between captures
capture_interval = 5  
# output folder for images
output_folder = f"./captures/{datetime.now().strftime("%Y%m%d_%H%M%S")}"

# create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# verify working dir
dir_cont = os.listdir()
if not "frame_recorder.py" in dir_cont:
    print("malformed working dir, please set absolutely")





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
