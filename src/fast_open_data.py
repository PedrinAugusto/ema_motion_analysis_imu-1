import numpy as np
import pandas as pd
import math
from pathlib import Path

import os
import sys
sys.path.append("../src")
from conversion_mat_to_py import mat2dict, pretty_dict, matobj2dict, dict2ntuple, name_data
from sources_cv2 import defineStartEnd, count_frames
from save_datas import save_data
from data_conversions import acc_to_angle
from filters import filter_butter


def open_data_filter(voluntary = 52, key = 'S1_Synched', freq_amostragem = 120, ordem = 2, freq_corte_Leg = 0.7,
                    freq_corte_Spine = 1.3, type_return = 'grau', angle_not_filter = False):
    '''Entrada: Número do voluntário -> int(1 até 90)'''
    '''Entrada: Nome da repetição -> str('S1_Synched', 'S2_Synched', 'I1', 'I2', 'S1', 'S2')'''
    '''Entrada: Frequência de amostragem -> int'''
    '''Entrada: Ordem do filtro butter -> int'''
    '''Entrada: Frequência de corte dos dados da perna -> int'''
    '''Entrada: Frequência de corte dos dados do tronco -> int'''
    '''Entrada: Tipo de retorno, grau, rad ou ambos -> str'''
    '''Saída: Ângulos dos dados -> shape(data_Spine,1), shape(data_Right_Leg,1), shape(data_Left_Leg,1)'''
    
    voluntary = str(voluntary)
    archive, name, sincro = name_data(voluntary, key)
    

    try:
    	data_path = '/Users/User/OneDrive/TCC/ema_motion_analysis_imu/dota/'
    	data = pd.read_csv(data_path + archive, sep = ';')
    except FileNotFoundError:
    	try:
    		sys.path.append("../data/")
    		data_path = '../data/'
    		path_and_archive = os.path.join(data_path, archive)
    		data = pd.read_csv(path_and_archive, sep = ';')
    		print('Exemplo do Git Hub')

    	except:
    		data_path_1 = os.getcwd()
    		sys.path.append("../data/")
    		data_path = '../data/'
    		path_and_archive = os.path.join(data_path, archive)
    		data = pd.read_csv(path_and_archive, sep = ';')
    		print('Exemplo do Git Hub 2')

    
    
    RightUpLeg = data.iloc[:,3:6].values
    LeftUpLeg = data.iloc[:,6:9].values
    Spine = data.iloc[:,15:18].values
    
    # Aplicando filtro com frequência de corte do pescoço, perna direita e perna esquerda.
    Spine_filter = filter_butter(Spine, ordem, freq_corte_Spine, freq_amostragem)
    RightUpLeg_filter = filter_butter(RightUpLeg, ordem, freq_corte_Leg, freq_amostragem)
    LeftUpLeg_filter = filter_butter(LeftUpLeg, ordem, freq_corte_Leg, freq_amostragem)
    
    # Aplicando a conversão de ângulos
    rad_Spine_filter, angle_Spine_filter = acc_to_angle(Spine_filter)
    rad_RightUpLeg_filter, angle_RightUpLeg_filter = acc_to_angle(RightUpLeg_filter)
    rad_LeftUpLeg_filter, angle_LeftUpLeg_filter = acc_to_angle(LeftUpLeg_filter)
    
    # Vetor de tempo
    t = np.linspace(0, len(angle_RightUpLeg_filter) / freq_amostragem, len(angle_RightUpLeg_filter))
    
    if angle_not_filter == True:
    	rad_Spine, angle_Spine = acc_to_angle(Spine)
    	rad_RightUpLeg, angle_RightUpLeg = acc_to_angle(RightUpLeg)
    	rad_LeftUpLeg, angle_LeftUpLeg = acc_to_angle(LeftUpLeg)

    	return angle_Spine, angle_RightUpLeg, angle_LeftUpLeg

    if type_return == 'grau':
        return angle_Spine_filter, angle_RightUpLeg_filter, angle_LeftUpLeg_filter
    if type_return == 'rad':
        return rad_Spine_filter, rad_RightUpLeg_filter, rad_LeftUpLeg_filter
    if type_return == 'grau_and_rad':
        return angle_Spine_filter, angle_RightUpLeg_filter, angle_LeftUpLeg_filter, rad_Spine_filter, rad_RightUpLeg_filter, rad_LeftUpLeg_filter
    
    else: 
        return False