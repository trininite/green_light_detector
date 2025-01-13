green light detector is an AI powered tool designed
for drivers to alert them of the switch of a traffic
light from red to green.

YOLOv11 is used as a base model
Additional training is done using ultralytics run by
python310
The trained model is converted to onnx format 
The onnx model is then converted to rknn format by
rknn-toolkit making the final model used in runtime
on the orange pi
local inference testing is performed before thr rknn
conversion
