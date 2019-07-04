import cv2
import re
import os
import glob
import pdb
import numpy as np
import pandas as pd
import shutil

devide_ary = np.array(pd.read_csv("devide.csv", header=None))
img_files = glob.glob("./rgb_raw/*.png")
dir_path = os.path.dirname(img_files[0])
save_path = "./rgb"

img_files = glob.glob("./rgb_1/*.png")
dir_path = os.path.dirname(img_files[0])

devide_ind = np.array(pd.read_csv("./devide.csv", header=None))

devide_count = 0
#save_path = "./rgb_1"
save_path = './' + str(devide_count)
if not os.path.exists(save_path):
    os.mkdir(save_path)
else :
    shutil.rmtree(save_path)
    os.mkdir(save_path)

file_count = 0
for i, _img_name in enumerate(img_files):
    devide_idx = devide_ind[devide_count]

    if i != devide_idx:
        img_name_full = _img_name
        img_name = os.path.basename(_img_name)
        pattern = '.*?(\d+)\D+(\d+).*'
        result = re.search(pattern, img_name)
        img_idx = result.group(1)
        img_time_stamp = result.group(2)
        copy_path = save_path + "/%06d_" %(file_count) + img_time_stamp + ".png"
        shutil.copyfile(img_name_full ,copy_path)
        file_count = file_count + 1
    else:
        devide_count = devide_count + 1
        save_path = './' + str(devide_count)
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        else :
            shutil.rmtree(save_path)
            os.mkdir(save_path)
        file_count = 0
        
#result_int = int(result.group(1))
#idxes = np.append(idxes, result_int)

    