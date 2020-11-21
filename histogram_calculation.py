import requests
import numpy as np
import cv2 as cv
import csv
from collections import defaultdict

image_url = 'https://www.researchgate.net/profile/Tao_Chen15/publication/3935609/figure/fig1/AS:394647298953219@1471102656485/8-bit-256-x-256-Grayscale-Lena-Image.png'

# Downloading the image
img_data = requests.get(image_url).content
with open('image.jpg', 'wb') as handler:
    handler.write(img_data)

    # Opening the image for reading
    img = cv.imread('image.jpg', 0)

    img_H = img.shape[0]
    img_W = img.shape[1]

    # List of zeros for containing the tonal values
    histogram = np.zeros([256], np.int32)

    # Counting and saving tonal values
    for r in range(img_H):
        for c in range(img_W):
            histogram[img[r, c]] += 1

    # Saving the color and it's tonal value to a dictionary
    dic = defaultdict(int)
    for i in range(len(histogram)):
        dic[i] = histogram[i]

    # Sort tonal values from high to low and save to csv
    with open('histogram.csv', 'w', newline='') as fp:

        writer = csv.writer(fp)
        writer.writerow(['color', 'tonal value'])
        for v in sorted(dic, key=dic.get, reverse=True):
            writer.writerow([v, dic[v]])
