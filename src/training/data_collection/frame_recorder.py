import cv2
import time
from datetime import datetime

# camera index (0 is usually the default camera)
camera_index = 0
# interval in seconds between captures
capture_interval = 5  
# output folder for images
output_folder = "./captures"

# create output folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# initialize camera
camera = cv2.VideoCapture(camera_index)
if not camera.isOpened():
    raise Exception("could not open camera")

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("failed to grab frame")
            break
        
        # generate timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_folder, f"{timestamp}.jpg")
        
        # save the frame
        cv2.imwrite(filename, frame)
        print(f"saved {filename}")
        
        # wait for the next capture
        time.sleep(capture_interval)

except KeyboardInterrupt:
    print("stopping capture...")

finally:
    camera.release()
    cv2.destroyAllWindows()
