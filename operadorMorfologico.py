#Aline Stolai 22.121.003-2
#João Lucas Rocha 22.121.004-2

import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

# Carregar imagens
img1 = cv2.imread('GIRAFA.jpeg')
img2 = cv2.imread('Satelite.jpeg')  # Nova imagem adicionada
img3 = cv2.imread('Aviao.jpeg')     # Nova imagem adicionada

# Converter para RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

# Aplicar filtro de ruído (blurring)
img1_blur = cv2.blur(img1, (5, 5))
img2_blur = cv2.blur(img2, (5, 5))
img3_blur = cv2.blur(img3, (5, 5))

# Converter para escala de cinza
img1_gray = cv2.cvtColor(img1_blur, cv2.COLOR_RGB2GRAY)
img2_gray = cv2.cvtColor(img2_blur, cv2.COLOR_RGB2GRAY)
img3_gray = cv2.cvtColor(img3_blur, cv2.COLOR_RGB2GRAY)

# Calcular limiar
a = img1_gray.max()
_, thresh1 = cv2.threshold(img1_gray, a/2+100, a, cv2.THRESH_BINARY_INV)
_, thresh2 = cv2.threshold(img2_gray, a/2+100, a, cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(img3_gray, a/2+100, a, cv2.THRESH_BINARY_INV)

# Preparar o kernel
kernel = np.ones((12, 12), np.uint8)

# Aplicar operadores morfológicos
img1_dilate = cv2.dilate(thresh1, kernel, iterations=1)
img1_erode = cv2.erode(thresh1, kernel, iterations=1)
img1_open = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
img1_close = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, kernel)
img1_grad = cv2.morphologyEx(thresh1, cv2.MORPH_GRADIENT, kernel)
img1_tophat = cv2.morphologyEx(thresh1, cv2.MORPH_TOPHAT, kernel)
img1_blackhat = cv2.morphologyEx(thresh1, cv2.MORPH_BLACKHAT, kernel)

# Aplicar operadores morfológicos para a segunda imagem
img2_dilate = cv2.dilate(thresh2, kernel, iterations=1)
img2_erode = cv2.erode(thresh2, kernel, iterations=1)
img2_open = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
img2_close = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)
img2_grad = cv2.morphologyEx(thresh2, cv2.MORPH_GRADIENT, kernel)
img2_tophat = cv2.morphologyEx(thresh2, cv2.MORPH_TOPHAT, kernel)
img2_blackhat = cv2.morphologyEx(thresh2, cv2.MORPH_BLACKHAT, kernel)

# Aplicar operadores morfológicos para a terceira imagem
img3_dilate = cv2.dilate(thresh3, kernel, iterations=1)
img3_erode = cv2.erode(thresh3, kernel, iterations=1)
img3_open = cv2.morphologyEx(thresh3, cv2.MORPH_OPEN, kernel)
img3_close = cv2.morphologyEx(thresh3, cv2.MORPH_CLOSE, kernel)
img3_grad = cv2.morphologyEx(thresh3, cv2.MORPH_GRADIENT, kernel)
img3_tophat = cv2.morphologyEx(thresh3, cv2.MORPH_TOPHAT, kernel)
img3_blackhat = cv2.morphologyEx(thresh3, cv2.MORPH_BLACKHAT, kernel)

# Plotar as imagens
imagens = [img1, img1_blur,  img1_gray, thresh1, img1_erode, img1_dilate, img1_open, img1_close, img1_grad,
          img1_tophat, img1_blackhat,
          img2, img2_blur,  img2_gray, thresh2, img2_erode, img2_dilate, img2_open, img2_close, img2_grad,
          img2_tophat, img2_blackhat,
          img3, img3_blur,  img3_gray, thresh3, img3_erode, img3_dilate, img3_open, img3_close, img3_grad,
          img3_tophat, img3_blackhat]

formatoX = math.ceil(len(imagens)**.5)
if (formatoX**2-len(imagens)) > formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX

for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i], 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()


