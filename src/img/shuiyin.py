#!/usr/bin/python
#-*- coding:cp936 -*-
import cv2
import os


def add_shuiyin(imput_img_path, output_img_path, shuiyin_img, shuiyin_pos):
    if(path.endswith(".jpg")):
        src_img = cv2.imread(imput_img_path).astype('float32')
        shuiyin_i = 0
        for i in range(shuiyin_pos[0], min(src_img.shape[0], shuiyin_pos[0] + shuiyin_img.shape[0])):
            shuiyin_j = 0
            for j in range(shuiyin_pos[1], min(src_img.shape[1], shuiyin_pos[1] + shuiyin_img.shape[1])):
                src_img[i][j][0] += shuiyin_img[shuiyin_i][shuiyin_j][0]
                src_img[i][j][1] += shuiyin_img[shuiyin_i][shuiyin_j][1]
                src_img[i][j][2] += shuiyin_img[shuiyin_i][shuiyin_j][2]
                if src_img[i][j][0] > 255:
                    src_img[i][j][0] = 255
                if src_img[i][j][1] > 255:
                    src_img[i][j][1] = 255
                if src_img[i][j][2] > 255:
                    src_img[i][j][2] = 255
                shuiyin_j += 1
            shuiyin_i += 1

        src_img = src_img.astype('uint8')
        cv2.imwrite(output_img_path, src_img)


src_dir = r"C:\Users\Administrator\Desktop\goods_imgs"
output_dir = r"C:\Users\Administrator\Desktop\shuiyin"

shuiyin_img = cv2.imread(r'C:\Users\Administrator\Desktop\shuiyin.jpg')
shuiyin_pos = (80, 80)

for path in os.listdir(src_dir):
    add_shuiyin(os.path.join(src_dir, path), os.path.join(output_dir, path), shuiyin_img, shuiyin_pos)
