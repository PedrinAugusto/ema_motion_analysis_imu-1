import numpy as np
import pandas as pd
import math


def save_data(data, key, name_discription):
    
    '''Dados do movimento de sentar e levantar para serem salvos'''
    '''Entrada: DataFrame com dados selecionados para o movimento de sentar e levantar'''
    
    caminho2 = '/Users/User/OneDrive/TCC/ema_motion_analysis_imu/data/'
    arquivo = name_discription +'_Sit_and_Stand.csv'
    
    data.to_csv(caminho2 + arquivo, sep = ';', index = False)