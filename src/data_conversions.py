import numpy as np
import pandas as pd
import math


def acc_to_angle(data):
    
    """Função de transformação de acelerações (x, y, z) em ângulos."""
    
    """Entrada: Lista com dados de aceleração com os 3 eixos (x, y, z) """
    """Saída: Lista com dados de ângulos em graus e radianos em relação ao eixo z"""


    # Separar os eixos 

    Ax = data[:,0]
    Ay = data[:,1]
    Az = data[:,2]

    # Módulo da força G 
    
    Gp = np.sqrt(np.power(Ax, 2) + np.power(Ay, 2) + np.power(Az, 2))

    
    # Encontrar o ângulo em relação ao eixo z com dados de teste   
    
    x = Az/Gp

    angle_rad = np.arccos(x)
    angle = np.rad2deg((np.arccos(x)))
    
    return angle_rad, angle



def sep_modo(data, estimated_data, modo_sequence, classes):
    
    
    V_seq = np.zeros(len(modo_sequence))
    Var_seq = np.zeros(len(modo_sequence))
    V_modo = np.zeros(len(classes))
    Var_modo = np.zeros(len(classes))
    
    modo = np.zeros((data.shape))

    for i in range(len(modo_sequence)):
        if i == 0:
            modo[:estimated_data[i]] = modo_sequence[i]
            V_seq[i] = np.mean(np.diff(data[:estimated_data[i]]))
            Var_seq[i] = np.var(np.diff(data[:estimated_data[i]]))
            
            
        elif i == (len(estimated_data)):
            modo[estimated_data[i-1]:] = modo_sequence[i]
            V_seq[i] = np.mean(np.diff(data[estimated_data[i-1]:]))
            Var_seq[i] = np.var(np.diff(data[estimated_data[i-1]:]))
        
        else:
            modo[estimated_data[i-1]:estimated_data[i]] = modo_sequence[i]
            V_seq[i] = np.mean(np.diff(data[estimated_data[i-1]:estimated_data[i]]))
            Var_seq[i] = np.var(np.diff(data[estimated_data[i-1]:estimated_data[i]]))
                    
    for n in range(len(classes)):
        idx = np.where(np.array(modo_sequence) == n+1)[0]
        V_modo[n] = np.mean(np.array(V_seq)[idx])
        Var_modo[n] = np.mean(np.array(Var_seq)[idx])
        
    return modo, V_seq, V_modo, Var_seq, Var_modo



def transition_matrix(modo, classes):
    
    transitions = np.zeros(modo.shape)
    not_transitions = np.zeros(modo.shape)
    transition_matrix = np.zeros([len(classes), len(classes)])
    

    for i in range(len(classes)):
        for j in range(len(classes)):
            for n in range(len(modo)-1):
                t = n + 1
                
                if (modo[t-1] == i+1 and modo[t] == j+1):
                    transitions[t] = 1

                else:
                    transitions[t] = 0

                if modo[t] == i+1:
                    not_transitions[t] = 1

                else:
                    not_transitions[t] = 0
            
            transition_matrix[i, j] = np.sum(transitions)/np.sum(not_transitions)
            #plt.plot(transitions, label = 'Transitions: '+str(i)+','+str(j))
            #plt.legend()
            #plt.show()
            #plt.plot(not_transitions, label = 'Not Transitions: '+str(i)+','+str(j))
            #plt.legend()
            #plt.show()
            
    return transition_matrix