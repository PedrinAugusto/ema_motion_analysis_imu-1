import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal as signal
from pathlib import Path
from scipy.signal import medfilt
from scipy.signal import sosfiltfilt, butter



def spectrum_periodogram_complete(data, freq_amostragem, grafico = 'pot', save = False):
    
    ''' Entrada: Dados com todos os sensores np.shape([:,0:27]) '''
    ''' Entrada: tipo de gráfico pot(somente o da densidade de potência), log(gráfico de densidade em log)'''
    '''          pot_log(Os dois gráficos). Por padrão será apenas o gráfico normal '''
    ''' Saídas: Gráficos de Densidade Espectral de Potência '''
    
    f_name = 'C:/Users/User/OneDrive/TCC/ema_motion_analysis_imu/Imagens/'

    eixos = ['eixo x', 'eixo y', 'eixo z']
    sensors_names = ['Hip', 'RightUpLeg', 'LeftUpLeg', 'Head', 'Neck', 'Spine3', 'Spine2', 'Spine1', 'Spine']
    

    if grafico == 'pot':
        for k in range(len(sensors_names)):
            plt.figure(figsize=[15,8])
            for i in range(len(eixos)):
                f, Pper_spec = signal.periodogram(data.iloc[:,k*3+i].values, freq_amostragem, 'flattop', scaling='density')
                plt.plot(f, Pper_spec, label = eixos[i])
            plt.legend()
            plt.title(sensors_names[k])
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Densidade Espectral de Potência')
            plt.grid()
            if save: plt.savefig(f_name + sensors_names[k] + 'complete_pot.png')
            plt.show()
            i = 0

            	
        
    if grafico == 'log':
        for k in range(len(sensors_names)):
            plt.figure(figsize=[15,8])
            for i in range(len(eixos)):
                f, Pper_spec = signal.periodogram(data.iloc[:,k*3+i].values, freq_amostragem, 'flattop', scaling='density')
                plt.semilogy(f, Pper_spec, label = eixos[i])
            plt.legend()
            plt.title(sensors_names[k])
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Densidade Espectral de Potência')
            plt.grid()
            if save: plt.savefig(f_name + sensors_names[k] + 'complete_log.png')
            plt.show()
            i = 0

            
            
    if grafico == 'pot_log':
        for k in range(len(sensors_names)):
            #plt.figure(figsize=[15,8])
            for i in range(len(eixos)):
                f, Pper_spec = signal.periodogram(data.iloc[:,k*3+i].values, freq_amostragem, 'flattop', scaling='density')
                plt.semilogy(f, Pper_spec, label = eixos[i])
            plt.legend()
            #plt.title(sensors_names[k])
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Densidade Espectral de Potência')
            plt.grid()
            if save: plt.savefig(f_name + sensors_names[k] + 'complete_log.png')
            plt.show()
            i = 0


            #plt.figure(figsize=[15,8])
            for j in range(len(eixos)):
                f, Pper_spec = signal.periodogram(data.iloc[:,k*3+j].values, freq_amostragem, 'flattop', scaling='density')
                plt.plot(f, Pper_spec, label = eixos[j])
            plt.legend()
            #plt.title(sensors_names[k])
            plt.xlabel('Frequência [Hz]')
            plt.ylabel('Densidade Espectral de Potência')
            plt.grid()
            if save: plt.savefig(f_name + sensors_names[k] + 'complete_pot.png')
            plt.show()
            i = 0



def spectrum_periodogram(data, freq_amostragem, title = 'Sem Título', save = False):
    f_name = 'C:/Users/User/OneDrive/TCC/ema_motion_analysis_imu/Imagens/'

    eixos = ['eixo x', 'eixo y', 'eixo z']
    #plt.figure(figsize=[15,8])
    for i in range(len(eixos)):
        f, Pper_spec = signal.periodogram(data[:,i], freq_amostragem, 'flattop', scaling='density')
        plt.plot(f, Pper_spec, label = eixos[i])
    plt.legend()
    #plt.title(title)
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Densidade Espectral de Potência')
    plt.grid()
    if save: plt.savefig(f_name + title + 'pot.png')
    plt.show()
    i = 0

            	
    
    #plt.figure(figsize=[15,8])
    for i in range(len(eixos)):
        f, Pper_spec = signal.periodogram(data[:,i], freq_amostragem, 'flattop', scaling='density')
        plt.semilogy(f, Pper_spec, label = eixos[i])
    plt.legend()
    #plt.title(title)
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Densidade Espectral de Potência')
    plt.grid()
    if save: plt.savefig(f_name + title + 'log.png')
    plt.show()
    i = 0




def spectrum_periodogram_reduced(data, freq_amostragem, title = 'Sem Título', save = False):
    f_name = 'C:/Users/User/OneDrive/TCC/ema_motion_analysis_imu/Imagens/'

    eixos = ['eixo x', 'eixo y', 'eixo z']
    #plt.figure(figsize=[15,8])
    for i in range(len(eixos)):
        f, Pper_spec = signal.periodogram(data[:,i], freq_amostragem, 'flattop', scaling='density')
        vetor_f = []
        vetor_Pper = []
        for j in range(len(f)):
            if f[j] < 5:
                vetor_f.append(f[j])
                vetor_Pper.append(Pper_spec[j])
        
        plt.plot(vetor_f, vetor_Pper, label = eixos[i])
    plt.legend()
    #plt.title(title)
    plt.xlabel('Frequência [Hz]')
    plt.ylabel('Densidade Espectral de Potência')
    plt.grid()
    if save: plt.savefig(f_name + title + 'reduced.png')
    plt.show()
    i = 0

    
    
    #for i in range(len(eixos)):
    #    f, Pper_spec = signal.periodogram(data[:,i], freq_amostragem, 'flattop', scaling='spectrum')
    #    vetor_f = []
    #    vetor_Pper = []
    #    for j in range(len(f)):
    #        if f[j] < 3:
    #            vetor_f.append(f[j])
    #            vetor_Pper.append(Pper_spec[j])
    #    
    #    plt.semilogy(vetor_f, vetor_Pper, label = eixos[i])
    #plt.legend()
    #plt.title(title)
    #plt.xlabel('Frequência [Hz]')
    #plt.ylabel('Densidade Espectral de Potência')
    #plt.grid()
    #plt.show()
    #i = 0



def plot_filter_butter(ordem, freq_corte, save = False):
    f_name = 'C:/Users/User/OneDrive/TCC/ema_motion_analysis_imu/Imagens/'

    b, a = signal.butter(ordem, freq_corte, 'low', analog=True)
    w, h = signal.freqs(b, a)
    title = 'Resposta em frequência do filtro Butterworth'
    #plt.figure(figsize=[15,8])
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title(title)
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(100, color='green') # cutoff frequency
    if save: plt.savefig(f_name + title + '.png')
    plt.show()

    
    	



def plot_comp_filter(t, data, data_filter, title = 'Sem Título', save = False):
    f_name = 'C:/Users/User/OneDrive/TCC/ema_motion_analysis_imu/Imagens/'

    #plt.figure(figsize=[15,8])

    plt.plot(t, data_filter, label = 'Sinal com filtragem')
    plt.plot(t, data, label = 'Sinal sem filtragem')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Ângulo (°)')
    plt.legend()
    #plt.title(title)
    plt.grid()
    if save: plt.savefig(f_name + title + '.png')
    plt.show()




