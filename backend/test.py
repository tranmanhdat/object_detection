import sys
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
from yolov5.model import *

if __name__ == "__main__":
    model = Yolov5(weights='/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5x6.pt', imgsz=(1280, 1280))
    text = model.inference('data_test/src/1.jpg', 'data_test/result/1.jpg', 'data_test/result/1.txt')