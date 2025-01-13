import os

from ultralytics import YOLO
from rknn.api import RKNN

model_path = "models/vanilla/yolo11n.pt"
onnx_path = "models/yolo11n.onnx"
rknn_path = "models/yolo11n.rknn"

def train_model() -> str:
    global model_path
    global onnx_path

    model = YOLO(model_path)
    model.train(data="datasets/traffic_lights/data.yaml", epochs=100)

    # Rename the previous trained model to .last if it exists
    if os.path.isfile(model_path):
        if os.path.isfile(f"{model_path}.last"):
            os.remove(f"{model_path}.last")
        os.rename(model_path, f"{model_path}.last")

    # Rename the previous onnx model to .last if it exists
    if os.path.isfile(onnx_path):
        if os.path.isfile(f"{onnx_path}.last"):
            os.remove(f"{onnx_path}.last")
        os.rename(onnx_path, f"{onnx_path}.last")

    # Save and export the model
    model.save(model_path)
    model.export(format="onnx", simplify=True, weights=onnx_path)

    return onnx_path

# should the model be retrained or just skip to export
train_bool = input("Do you want to train? (y/N): ")
if train_bool in {"y", "Y"}:
    onnx_path = train_model()
else:
    onnx_path = "models/yolo11n.onnx"
del(train_bool)

# configure rknn
rknn = RKNN()
print('--> configuring model') 
rknn.config(mean_values=[[0, 0, 0]], std_values=[[1, 1, 1]], target_platform="rk3588")
print('done')

# load onnx model
print('--> loading onnx model')
ret = rknn.load_onnx(model=onnx_path)
if ret != 0:
    print('load onnx model failed')
    exit(ret)
print('done')

# convert to rknn
print('--> building model')
ret = rknn.build(do_quantization=False)  # set `do_quantization=True` if quantization is needed
if ret != 0:
    print('build rknn model failed')
    exit(ret)
print('done')

# export to rknn
if os.path.isfile(rknn_path):
    if os.path.isfile(f"{rknn_path}.last"):
        os.remove(f"{rknn_path}.last")
    os.rename(rknn_path, f"{rknn_path}.last")
if rknn.export_rknn(rknn_path) != 0:
    print(f"Exporting {rknn_path} failed")
    exit(1)
print(f"Model exported successfully to {rknn_path}")


