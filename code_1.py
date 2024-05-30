import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Definir las funciones de los filtros
def apply_mean_filter(img):
    return cv2.blur(img, (5,5))

def apply_median_filter(img):
    return cv2.medianBlur(img, 5)

def apply_laplacian_filter(img):
    laplacian_filter = cv2.Laplacian(img, cv2.CV_64F)
    return np.uint8(np.absolute(laplacian_filter))

def apply_sobel_filter_x(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    return sobelx

def apply_sobel_filter_y(img):
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    return sobely

# Función para cargar la imagen
def load_image():
    global img, img_label, original_img_label
    filepath = filedialog.askopenfilename()
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img))
    original_img_label.config(image=img_tk)
    original_img_label.image = img_tk
    img_label.config(image=img_tk)
    img_label.image = img_tk

# Función para mostrar la imagen
def show_image(img, title):
    img_tk = ImageTk.PhotoImage(Image.fromarray(img))
    img_label.config(image=img_tk)
    img_label.image = img_tk

# Crear la interfaz gráfica
root = Tk()
root.geometry("800x600")  # Cambia "800x600" por el tamaño que prefieras

current_filter_label = ttk.Label(root, text="")
current_filter_label.grid(row=6, column=0, pady=10, padx=10)

# Crear los botones para cada filtro
ttk.Button(root, text="Cargar imagen", command=load_image).grid(row=0, column=0, pady=60, padx=10, sticky='ns')
ttk.Button(root, text="Aplicar filtro de media", command=lambda: (current_filter_label.config(text="Aplicando filtro de media"), show_image(apply_mean_filter(img), 'Media'))).grid(row=1, column=0, pady=15, padx=40)
ttk.Button(root, text="Aplicar filtro de mediana", command=lambda: (current_filter_label.config(text="Aplicando filtro de mediana"), show_image(apply_median_filter(img), 'Mediana'))).grid(row=2, column=0, pady=15, padx=40)
ttk.Button(root, text="Aplicar filtro Laplaciano", command=lambda: (current_filter_label.config(text="Aplicando filtro Laplaciano"), show_image(apply_laplacian_filter(img), 'Laplaciano'))).grid(row=3, column=0, pady=15, padx=40)
ttk.Button(root, text="Aplicar filtro Sobel X", command=lambda: (current_filter_label.config(text="Aplicando filtro Sobel X"), show_image(apply_sobel_filter_x(img), 'Sobel X'))).grid(row=4, column=0, pady=15, padx=40)
ttk.Button(root, text="Aplicar filtro Sobel Y", command=lambda: (current_filter_label.config(text="Aplicando filtro Sobel Y"), show_image(apply_sobel_filter_y(img), 'Sobel Y'))).grid(row=5, column=0, pady=15, padx=40)

ttk.Label(root, text="Imagen original", background='gray', foreground='white').grid(row=0, column=1, padx=50, pady=10)
original_img_label = ttk.Label(root)
original_img_label.grid(row=1, column=1, rowspan=6, padx=10, pady=10)

ttk.Label(root, text="Imagen con filtro aplicado", background='gray', foreground='white').grid(row=0, column=2, padx=50, pady=10)
img_label = ttk.Label(root)
img_label.grid(row=1, column=2, rowspan=6, padx=10, pady=10)

root.mainloop()


