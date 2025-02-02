green light detector is an AI powered tool designed
for drivers to alert them of the switch of a traffic
light from red to green.

YOLOv11 is used as a base model
Additional training is done using ultralytics run by
python312
The trained model is converted to onnx format 
The onnx model is then converted to rknn format by
rknn-toolkit making the final model used in runtime
on the orange pi
local inference testing is performed before thr rknn
conversion

TODO:
 create docker environment for training


ramblings:
current webcam has bad dynamic range, cant capture both traffic lights and the
road at night could be fine if i use cv to create a brightness mask then lower
exposure and recapture and look in bounding boxes around the over threshhold
sections. 
possible loop:
    - based on time and/or ambient light sensor change to day or night mode (night mode
    for this example as it really only does extra stuff compared to day, not anything
    different) this should update once every 15 min or so

    - wait speed = 0mph

    - first pic will be taken at defualt exposure so if there is a traffic light, it will
    be very overexposed and blown out. use cv2 to create a pixel mask based on a threshold
    brightness (#FFF might work as the cam way overexposes the lights trying to keep the road
    visible)

    - bounding boxes will be calculated for each high exposure region on the mask of a cetain 
    size. take a picture with lower exposure, look at the bounded region and infer until there
    is a confident answer.

    - create human readable result with bounding boxes and class tags and save with date and time

    - watch bounded area that the traffic light is in at the right exposure at and increased interval
    wait until the light is green (maybe just until its not red)





    - start taking pictures at a set rate either based on estimated distance travelled,
    at set speed intervals, or just a flat time. for each picture all following steps
    should run in a seperate thread. the camera should continue taking pictures on the 
    main thread, with the exposure set to the average of exposure requests from all
    threads, until the infrencer has a confident answer or the vehicle speed exceeds 
    the threshold