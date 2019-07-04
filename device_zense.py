import cv2
import re
import os
import glob
import pdb
import numpy as np
import pandas as pd
import shutil

#後でタイムスタンプ処理加える事
_files = glob.glob("./data/*.pcd")
total_file_num = len(_files)
max_idx_num = total_file_num

devide_idxs = np.array(pd.read_csv("./devide.csv", header=None))
#devide_idxs_max = len(devide_idxs)

color_img_files = glob.glob("./data/color_*.jpg")
color_img_files = np.sort(color_img_files)
depth_img_files = glob.glob("./data/depth_*.png")
depth_img_files = np.sort(depth_img_files)
depth_color_img_files = glob.glob("./data/depth_color_*.jpg")
depth_color_img_files = np.sort(depth_color_img_files)
pcd_files = glob.glob("./data/*.pcd")
pcd_files = np.sort(pcd_files)

devide_count = 0
save_path = './' + str(devide_count)
if not os.path.exists(save_path):
    os.mkdir(save_path)
else :
    shutil.rmtree(save_path)
    os.mkdir(save_path)

file_count = 0

for i in np.arange(int(max_idx_num/5)): #連射回数分割る
    devide_idx = int(devide_idxs[devide_count]/5)
    print(i)
    if i != devide_idx:
        for shift in np.arange(5):
            color_img_name_full = color_img_files[i*5 + shift]
            depth_img_name_full = depth_img_files[i*5 + shift]
            depth_color_img_name_full = depth_color_img_files[i*5 + shift]
            pcd_file = pcd_files[i*5 + shift]
            #ファイルが正常にソートされているか確認

            color_img_name = os.path.basename(color_img_name_full)
            #pattern = '.*?(\d+)\D+(\d+).*' //with_timestamp
            pattern = '.*?(\d+).*'
            result = re.search(pattern, color_img_name)
            zfill_idx = result.group(1)
            #time_stamp = result.group(2)

            '''
            color_save_path = save_path + "/color_%06d_" %(file_count*5) + time_stamp + ".jpg"
            depth_save_path = save_path + "/depth_%06d_" %(file_count*5) + time_stamp + ".png"
            depth_color_save_path = save_path + "/depth_color_%06d_" %(file_count*5) + time_stamp + ".jpg"
            pcd_path = save_path + "/point_%06d_" %(file_count*5) + time_stamp + ".pcd"
            '''
            color_save_path = save_path + "/color_%06d_" %(file_count*5 + shift) + ".jpg"
            depth_save_path = save_path + "/depth_%06d_" %(file_count*5 + shift) + ".png"
            depth_color_save_path = save_path + "/depth_color_%06d_" %(file_count*5 + shift) + ".jpg"
            pcd_path = save_path + "/point_%06d_" %(file_count*5) + ".pcd"

            shutil.copyfile(color_img_name_full ,color_save_path)
            shutil.copyfile(depth_img_name_full ,depth_save_path)
            shutil.copyfile(depth_color_img_name_full ,depth_color_save_path)
            shutil.copyfile(pcd_file ,pcd_path)
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

    