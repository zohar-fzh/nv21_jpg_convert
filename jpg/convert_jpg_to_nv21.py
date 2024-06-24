
import cv2
import numpy as np
import os

def jpg_to_nv21(jpg_path, nv21_path, width=640, height=480):
    bgr_image = cv2.imread(jpg_path)
    bgr_image_resized = cv2.resize(bgr_image, (width, height))
    yuv_image = cv2.cvtColor(bgr_image_resized, cv2.COLOR_RGB2YUV)
    Y = yuv_image[:, :, 0]
    U = yuv_image[:, :, 1]
    V = yuv_image[:, :, 2]

    nv21_data = np.zeros((width * height * 3 // 2), dtype=np.uint8)
    nv21_data[:width * height] = Y.flatten()
    for i in range(0, height, 2):
        for j in range(0, width, 2):
            if j / 2 == 0: continue
            nv21_data[width * height + i // 2 * width + j] = U[i, j]
            nv21_data[width * height + i // 2 * width + j + 1] = V[i, j]

    with open(nv21_path, 'wb') as f:
        f.write(nv21_data.tobytes())

file_list = os.listdir('.')
for filename in file_list:
    if filename.lower().endswith('.jpg'):
        jpg_path = filename
        nv21_path = filename[:-4] + '.NV21'
        jpg_to_nv21(jpg_path, nv21_path)
