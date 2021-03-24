import os
import collections
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal as signal

from scipy.signal import medfilt
from scipy.signal import sosfiltfilt, butter



def filter_butter(data, ordem, freq_corte, freq_amostragem):
	''' Entrada: Dados que serão filtrados - shape(n,3)'''
	''' Entrada: Ordem do filtro'''
	''' Entrada: Frequência de corte do filtro'''
	''' Entrada: Frequência de amostragem do filtro'''
	''' Saída: Dados filtrados - shape(n,3)'''
    
    # Criar o filtro
	create_filter = signal.butter(ordem, freq_corte, btype='low', fs=freq_amostragem, output='sos')

    # Criar a variável que irá receber os dados filtrados
	data_filter = np.zeros(data.shape)
    
    # Aplicar o filtro
	data_filter[:,0] = signal.sosfiltfilt(create_filter, data[:,0])
	data_filter[:,1] = signal.sosfiltfilt(create_filter, data[:,1])
	data_filter[:,2] = signal.sosfiltfilt(create_filter, data[:,2])
    
	return data_filter  


def mean_filter(data, number_of_points, step=1):
	''' Entrada: Vetor de dados que serão filtrados = data(n,1) '''
	''' Saída: Vetor de dados filtrados = mean_feature(n,1)'''

	mean_feature = []
	for i in range(0, number_of_points):
		mean_feature.append(np.mean(data[0: i+1]))
	if number_of_points > 1:
		for i in range(0, len(data) - number_of_points, step):
			mean_feature.append(
                np.mean(data[i: number_of_points + i]))
	else:
		return data
	return np.array(mean_feature)


