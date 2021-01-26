import numpy as np
import pandas as pd
import math


def acc_to_angle(data):
    
    """Função de transformação de acelerações (x, y, z) em ângulos."""
    
    """Entrada: Lista com dados de aceleração com os 3 eixos (x, y, z) """
    """Saída: Lista com dados de ângulos em graus e radianos em relação ao eixo z"""


    # Separar os eixos 

    Ax = data[:,:1]
    Ay = data[:,1:2]
    Az = data[:,2:3]

    # Módulo da força G 
    
    Gp = np.sqrt(np.power(Ax, 2) + np.power(Ay, 2) + np.power(Az, 2))

    
    # Encontrar o ângulo em relação ao eixo z com dados de teste   
    
    x = Az/Gp

    angle_rad = np.arccos(x)
    angle = np.rad2deg((np.arccos(x)))
    
    return angle_rad, angle