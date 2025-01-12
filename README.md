green light detector is an AI powered tool designed
for drivers to alert them of the switch of a traffic
light from red to green.

Software and Dependencies
VSCode is recommended to allow standard use of dev
containers
YOLOv8 is used as a base model
Additional training is done using pytorch run by
python310
The trained model is converted to onnx format by
pytorch
The onnx model is then converted to rknn format by
rknn-toolkit making the final model used in runtime

