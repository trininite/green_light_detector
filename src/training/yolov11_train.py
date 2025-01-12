from ultralytics import YOLO
from rknn.api import RKNN

model = YOLO("src/models/yolo11n.pt")
from os import listdir
print(listdir())
model.train(data="datasets/traffic_lights/data.yaml", epochs=100)

model.export(format="onnx", simplify=True)

#rknn = RKNN()




#if input("Do you want to export to rknn? (y/N): ") in {"y", "Y"}:
#   model.export(format="onnx", simplify=True)
#   print("not implemented")
