import sys
from pathlib import Path
from time import time

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
sys.path.append(str('/home/trandat/project/p51/object_detection/'))  # add models/ to PATH
from yolov5.model_folder import *

if __name__ == "__main__":
    src_folder = '/mnt/Documents/P51/project/object_detection/Image_200'
    save_folder = '/mnt/Documents/P51/project/object_detection'
    models = ['/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5l.pt', 
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5l6.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5m.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5m6.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5n.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5n6.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5s.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5s6.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5x.pt',
              '/home/trandat/project/p51/object_detection/backend/pretrained_models/yolov5x6.pt',
              ]
    imgsz = [(640, 640),
             (1280, 1280),
             (640, 640),
             (1280, 1280),
             (640, 640),
             (1280, 1280),
             (640, 640),
             (1280, 1280),
             (640, 640),
             (1280, 1280)
             ]
    for model_path, size in zip(models, imgsz):
        model = Yolov5(weights=model_path, imgsz=size)
        p = Path(model_path)  # to Path
        save_path = os.path.join(save_folder ,p.stem)
        os.makedirs(save_path, exist_ok=True)
        for sub_folder in os.listdir(src_folder):
            try:
                print("Processing folder: ", sub_folder, model_path)
                sub_folder_path = os.path.join(src_folder, sub_folder)
                sub_dst_folder = os.path.join(save_path, sub_folder)
                os.makedirs(sub_dst_folder, exist_ok=True)
                img_dst_folder = os.path.join(sub_dst_folder, 'img')
                if os.path.exists(img_dst_folder):
                    continue
                os.makedirs(img_dst_folder, exist_ok=True)
                txt_dst_folder = os.path.join(sub_dst_folder, 'txt')
                os.makedirs(txt_dst_folder, exist_ok=True)
                info = model.inference(sub_folder_path, img_dst_folder, txt_dst_folder)
                with open(os.path.join(save_path, "runtime.txt"), 'a') as f_runtime:
                    f_runtime.write(str(sub_folder)+"\n"+str(info)+"\n")
            except Exception as e:
                print("Error: ", e)