import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

"""Codi per generar les fitxes del parchis
"""

#Constants
IM_SIZE = 255
RADIUS = 125

def generate_circular_matrix(arr, size: int, r: int):
    center = size // 2
    for i in range(size):
        for j in range(size):
            distancia = math.sqrt((i - center)**2 + (j - center)**2)
            if distancia > r:
                arr[i][j] = 0

def generate_RGBA_circular_matrix(RGBA_matrix: object, img_size: int, circle_radius: int):
    assert (RGBA_matrix.shape == (IM_SIZE, IM_SIZE, 4))

    #Number of channels
    for i in range(3):
        RGBA_channel = RGBA_matrix[:, :, i]
        RGBA_channel = generate_circular_matrix(RGBA_channel, img_size, circle_radius)

def generate_alpha_channel(RGBA_matrix: object, size: int):
    for i  in range(size):
        for j in range(size):
            if (RGBA_matrix[:,:,0][i][j] == 0 and \
                RGBA_matrix[:,:,1][i][j] == 0 and \
                RGBA_matrix[:,:,2][i][j] == 0):
                RGBA_matrix[:,:,3][i][j] = 0

def generate_RBGA_matrix(size: int, R: float = 0, G:float = 0, B: float = 0):
    img = np.ones([size, size, 4], dtype=np.uint8)
    img[:,:,0] = R   * img[:,:,0]
    img[:,:,1] = G   * img[:,:,1]
    img[:,:,2] = B   * img[:,:,2]
    img[:,:,3] = 255 * img[:,:,3] #Null Transparency
    return img

def main(R: int = 255, G: int = 255, B: int = 255, file_name: str = "circle.png"):
    #GENERATE IMAGE MATRIX
    im = generate_RBGA_matrix(IM_SIZE, R, G, B)
    generate_RGBA_circular_matrix(im, IM_SIZE, RADIUS)
    generate_alpha_channel(im, IM_SIZE)

    #LOAD IMAGE FROM NP MATRIX
    piece = Image.fromarray(im)
    piece.convert("RGBA")

    #SAVE IMG TO FILE
    piece.save(file_name, "PNG")

main(R = 250,
     G = 253,
     B = 15,
     file_name="fitxa_groga.png")







