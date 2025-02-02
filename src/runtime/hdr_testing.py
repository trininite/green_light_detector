import sys
import cv2
from pathlib import Path
from os import getcwd


# append the src directory to sys.path
sys.path.append("./src")

from common.camera_init import cam_init_wizard



# initialize camera
cap = cam_init_wizard()

# set exposure (negative values may indicate 'auto' mode)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0) # manual mode

img_count = 0
while True:
    cap.set(cv2.CAP_PROP_EXPOSURE, img_count)
    ret, frame = cap.read()
    if not ret:
        print("error: could not read frame")
        break
    
    cv2.imwrite(str(f"{getcwd()}/src/runtime/test/{img_count}.jpg"), frame)

    
    img_count += 1

cap.release()
cv2.destroyAllWindows()
