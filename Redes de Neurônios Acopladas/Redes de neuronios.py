import numpy as np
import matplotlib.pyplot as plt
from random import randrange
import math

#Variáveis
n = 500   # Quantidade de Neurônios da Simulação
contAtivos = 50  # Quantidade de Neurônios Ativos
ativo = 0.2       
inativo = -0.02 
DT = 0.01  # Variação do Tempo 
T_MAX = 200  #Tempo Máximo da Simulação
x = 0
y = 1
I = 2     # Corrente de Entrada (Estímulo Externo)
Si = 3    # Acoplamento
w = 0.1   # Influência (o quanto um neurônio pode influenciar os demais)
Alpha = 6
Beta = 0.1
Epsilon = 0.02
theta = 0.5  # Limiar de Corte
k = 2
T = np.arange(0, T_MAX, DT)  # Array de Intervalos - do instante 0 ao T_MAX
T_plot = np.arange(0, 2000, DT)
vetX = []
vetY = []

def criaMNeuronios():

    matriz_Neuronios = []

    return matriz_Neuronios


def iniciaNeuronios(matriz):
    i = 0

    # define a parte dos neurônios ativos (250 de 500)
    for i in range(i, contAtivos, 1):
        
        vetX = []
        vetY = []

        x_euler = np.random.uniform(-2, 2)
        y_euler = np.random.uniform(0, 4)

        vetX.append(x_euler)
        vetY.append(y_euler)

        vetor = [x_euler, y_euler, ativo, 0, vetX, vetY]
        matriz.append(vetor)

    # define a parte dos neurônios inativos (250 de 500)
    for i in range(contAtivos, n, 1):

        vetX = []
        vetY = []

        x_euler = np.random.uniform(-2, 2)
        y_euler = np.random.uniform(0, 4)

        vetX.append(x_euler)
        vetY.append(y_euler)

        vetor = [x_euler, y_euler, inativo, 0, vetX, vetY]
        matriz.append(vetor)

    return matriz

        
def calculaPotencial(matriz):
    for t in range(1, len(T)):
        if(T[t].is_integer()): print(T[t])
        for i in range(n):

            prev_neuron = matriz[(i-1)%n]  # pega o neurônio anterior
            neuron = matriz[i]
            pos_neuron = matriz[(i+1)%n]   # pega o neurônio posterior

            neuron[Si] = 0

            if ((prev_neuron[4][t-1] > theta)):
                neuron[Si] += w     # se Si = 1 influência 100% se Si = 0 nenhuma influência
            if ((pos_neuron[4][t-1] > theta)):
                neuron[Si] += w


                
        for i in range(n):
            neuron = matriz[i]
            x_ant = neuron[4][t-1]
            y_ant = neuron[5][t-1]
            
            deltaX = (((3 * x_ant) - (pow(x_ant, 3)) + 2 - y_ant + neuron[Si] + neuron[I]) * DT)

            deltaY = (Epsilon * (Alpha * (1 + math.tanh(x_ant / Beta)) - y_ant) * DT)

            neuron[4].append(x_ant + deltaX)
            neuron[5].append(y_ant + deltaY)
        
    return matriz

if __name__ == "__main__":

    matrizNeuronios = criaMNeuronios()

    matriz = iniciaNeuronios(matrizNeuronios)

    matriz_final = calculaPotencial(matriz)


for i in range(n):
    plt.plot()
    plt.plot(T, matriz_final[i][4])

# amostra = matriz_final[:20]

# for i in range(len(amostra)):
#     plt.plot()
#     plt.plot(T_plot, amostra[i])
    

plt.show()
