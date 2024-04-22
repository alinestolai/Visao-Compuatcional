#Aline Stolai 22.121.003-2
#João Lucas Rocha 22.121.004-2

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Função para processar uma imagem
def processar_imagem(imagem):
    # Convertendo para RGB
    img = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # Convertendo para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Segmentação de imagem
    a = img_gray.max()
    _, thresh = cv2.threshold(img_gray, a/2*1.7, a, cv2.THRESH_BINARY_INV)

    # Tamanho do kernel
    tamanhoKernel = 5
    kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)

    # Abertura morfológica
    thresh_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Filtro de ruído (blur)
    img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel, tamanhoKernel))

    # Detecção de bordas com Canny
    edges_gray = cv2.Canny(image=img_gray, threshold1=a/2, threshold2=a/2)
    edges_blur = cv2.Canny(image=img_blur, threshold1=a/2, threshold2=a/2)

    # Encontrar contornos
    contours, hierarchy = cv2.findContours(
                                   image=thresh,
                                   mode=cv2.RETR_TREE,
                                   method=cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    img_copy = img.copy()
    final = cv2.drawContours(img_copy, contours, contourIdx=-1,
                             color=(255, 0, 0), thickness=2)

    return img, img_blur, img_gray, edges_gray, edges_blur, thresh, thresh_open, final

# Carregar imagens
imagens = []
imagens_nomes = ['GIRAFA.jpeg', 'Satelite.jpeg', 'Aviao.jpeg']
for nome in imagens_nomes:
    img = cv2.imread(nome)
    imagens.append(img)

# Processar e plotar imagens
for imagem in imagens:
    processadas = processar_imagem(imagem)
    for i in range(len(processadas)):
        plt.subplot(len(imagens), 3, i + 1)
        plt.imshow(processadas[i], 'gray')
        plt.xticks([]), plt.yticks([])
    plt.show()
