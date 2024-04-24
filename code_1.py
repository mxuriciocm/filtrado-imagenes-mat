import cv2
import numpy as np
from matplotlib import pyplot as plt

# Cargar la imagen
img = cv2.imread('filtroRuido.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error al cargar la imagen.")
else:
    # Aplicar filtro de media
    mean_filter = cv2.blur(img, (5,5))

    # Aplicar filtro de mediana
    median_filter = cv2.medianBlur(img, 5)

    # Aplicar filtro Laplaciano
    laplacian_filter = cv2.Laplacian(img, cv2.CV_64F)
    laplacian_filter = np.uint8(np.absolute(laplacian_filter))

    # Aplicar filtro Sobel
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y
    sobelx = np.uint8(np.absolute(sobelx))
    sobely = np.uint8(np.absolute(sobely))

    # Mostrar las imágenes
    plt.figure(figsize=(12, 8))
    plt.subplot(2,3,1),plt.imshow(img, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,2),plt.imshow(mean_filter, cmap = 'gray')
    plt.title('Media'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(median_filter, cmap = 'gray')
    plt.title('Mediana'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,4),plt.imshow(laplacian_filter, cmap = 'gray')
    plt.title('Laplaciano'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,5),plt.imshow(sobelx, cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,6),plt.imshow(sobely, cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()
