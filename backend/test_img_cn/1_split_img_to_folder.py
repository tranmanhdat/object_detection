import sys
import os
import shutil

if __name__ == "__main__":
    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]
    os.makedirs(dst_folder, exist_ok=True)
    start_idx = 100000
    sub_folder = 'A' + str(start_idx)
    files = os.listdir(src_folder)
    for idx, file in enumerate(files):
        if idx%200 == 0:
            sub_folder = 'A' + str(start_idx + idx//200)
            sub_folder_path = os.path.join(dst_folder, sub_folder)
            if os.path.exists(sub_folder_path):
                shutil.rmtree(sub_folder_path)
            os.mkdir(sub_folder_path)
        src_file = os.path.join(src_folder, file)
        dst_file = os.path.join(sub_folder_path, file)
        shutil.copyfile(src_file, dst_file)