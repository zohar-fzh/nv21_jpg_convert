
import cv2
import numpy as np
import os

def nv21_to_jpg(nv21_data, width, height, output_path):
    yuv_image = np.frombuffer(nv21_data, np.uint8)
    yuv_image = yuv_image.reshape((height + height // 2, width))
    bgr_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR_NV21)
    cv2.imwrite(output_path, bgr_image)

file_list = os.listdir('.')
for filename in file_list:
    if filename.lower().endswith('.nv21'):
        with open(filename, 'rb') as f:
            nv21_data = f.read()
        width = 640
        height = 480
        output_path = filename[:-5] + '.jpg'
        nv21_to_jpg(nv21_data, width, height, output_path)
