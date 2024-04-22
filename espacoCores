#Aline Stolai 22.121.003-2
#João Lucas Rocha 22.121.004-0

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carregans imagem
img = cv2.imread('Aviao.jpeg')
img2 = cv2.imread('Satelite.jpeg')
img3 = cv2.imread('GIRAFA.jpeg')


# Convertendo espaço de cores
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img2_hls = cv2.cvtColor(img2, cv2.COLOR_BGR2HLS)

img3_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img3_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img3_hsv = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
img3_hls = cv2.cvtColor(img3, cv2.COLOR_BGR2HLS)

#plot imagens
imagens = [img_rgb,img_gray,img_hsv,img_hls,img2_rgb,img2_gray,img2_hsv,img2_hls,img3_rgb,img3_gray,img3_hsv,img3_hls]

for i in range(12):
    plt.subplot(3,4,i+1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()
plt.show()
