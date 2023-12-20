import os
from PIL import Image
from ultralytics import YOLO
import torch
import cv2

desired_label_empty = 0  # Replace with the label you want to count for empty spaces
desired_label_occupied = (
    1  # Replace with the label you want to count for occupied spaces
)

# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model_path = os.path.join("..", "weights", "shortbest.pt")

# Load a model
model = YOLO(model_path)  # load a custom model

im1 = cv2.imread("geknipt.png")
# im1 = cv2.imread("2013-02-26_15_09_35.jpg")
# im1 = cv2.imread("testparking.png")
# im1 = cv2.resize(im1, (640, 640))
results = model.predict(
    source=im1, save=True, show_labels=True
)  # save plotted images   # save predictions as labels       show_labels=False, show_conf=False,

# Initialize counters for both labels
total_boxes_empty = 0
total_boxes_occupied = 0

# Iterate through each detection and count occurrences of the desired labels
for detection in results:
    # Retrieve class labels from the detection.boxes.cls tensor
    labels_tensor = detection.boxes.cls

    # Convert the tensor to a Python list
    class_labels = (
        labels_tensor.cpu().numpy().tolist() if torch.is_tensor(labels_tensor) else []
    )

    # Count occurrences of desired labels within the class labels
    total_boxes_empty += class_labels.count(desired_label_empty)
    total_boxes_occupied += class_labels.count(desired_label_occupied)

print(f"Total number of empty spaces boxes detected: {total_boxes_empty}")
print(f"Total number of occupied spaces boxes detected: {total_boxes_occupied}")
