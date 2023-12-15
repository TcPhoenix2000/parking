from ultralytics import YOLO
import os
from PIL import Image
import torch

data_path = 'data.yaml'
absolute_path = os.path.abspath(data_path)
print(f"Absolute path to 'data.yaml': {absolute_path}")


os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# model yolo v5s

# Load a model and train it with gpu

model = YOLO('yolov5s.yaml') # yolov5s.yaml
results = model.train(data=absolute_path, epochs=10 )         #100 for finaal training

# results = model.train(data='../data.yaml', epochs=100)         #100 for finaal training