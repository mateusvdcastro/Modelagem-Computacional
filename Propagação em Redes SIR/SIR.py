from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import random

"""
Simulação Covid 19

S = Suscetíveis
I = Infectados
R = Recuperados
r = taxa de infecção
a = taxa de recuperados

dS/dt = -rSI => Taxa de indivíduos Suscetíveis
dI/dt = rSI - aI => Taxa de indivíduos Infectados
dR/dt = aI => Taxa de indivíduos Recuperados

S.N = S.No + (-rSI)dt => População de indivíduos Suscetíveis
S.I = S.i0 + (rSI - aI)dt => População de indivíduos Infectados
dR/dt = S.Ro + (aI)dt => População de indivíduos Recuperados

dS/dt + dI/dt + dR/dt = 0


Cenário Inicial t = 0:
S(0) = So         So + Io = N
I(0) = Io
R(0) = 0

considerando os valores de r, a, S0 e I0, haverá
uma epidemia?

Basicamente, precisamos avaliar se I(t) > Io

Avaliar a evolução de I

1) Se S < a/r temos: dI/dt < 0  
2) Se S > a/r temos: dI/dt > 0
"""

t = 10000
deltaT = 0.01
T = np.arange(0, t * 0.01, deltaT)

vacina = True
#Beta é a probabilidade de recuperação pós vacinação
beta = 0.1

class ModeloSIRCidade:
  def __init__(self, r, alfa, S, I):  ##Trocar o nome das Variáveis depois
    self.r = r #Taxa de Infecção
    self.alfa = alfa #Taxa de recuperação
    self.S = S
    self.I = I
    self.R = 0
    #S_0 + I_0 = N
    self.popSuscetiveis = [S]
    self.popInfectados = [I]
    self.popRecuperados = [0]


def Plot_Geral(popS, popI, popR):
    if (vacina == False):
        plt.plot(T, popS, label='População de Suscetíveis')
        plt.plot(T, popI, label='População de Infectados')
        plt.plot(T, popR, label='População de Recuperados')
        plt.xlabel('Tempo')
        plt.ylabel('Populações')
        plt.title("Simulação Covid-19")
        plt.legend()
        plt.show()
    else:
        plt.plot(T, popS, label='População de Suscetíveis')
        plt.plot(T, popI, label='População de Infectados')
        plt.plot(T, popR, label='População de Recuperados')
        plt.xlabel('Tempo')
        plt.ylabel('Populações')
        plt.title(f"Simulação Covid-19 com vacinação ({round(beta*100)}% de taxa de recuperação)")
        plt.legend()
        plt.show() 



if __name__ == "__main__":

    mod = ModeloSIRCidade(0.0001, 0.005, 5000, 100)

    i = 0

    if (vacina == True):
        while (i < t-1):

            i += 1

            dS = (-mod.r*mod.popSuscetiveis[i - 1]*mod.popInfectados[i - 1] - beta*mod.popSuscetiveis[i - 1])*deltaT
            mod.S = mod.popSuscetiveis[i - 1] + dS

            if (mod.S < 0):
                mod.S = 0 

            dI = (mod.r*mod.popSuscetiveis[i - 1]*mod.popInfectados[i - 1] - mod.alfa*mod.popInfectados[i - 1])*deltaT

            mod.I = mod.popInfectados[i - 1] + dI

            if (mod.I < 0):
                mod.I = 0

            dR = (mod.alfa*mod.popInfectados[i - 1] + beta*mod.popSuscetiveis[i - 1])*deltaT

            mod.R = mod.popRecuperados[i - 1] + dR

            if (mod.R < 0):
                mod.R = 0

            mod.popRecuperados.append(mod.R)
            mod.popInfectados.append(mod.I)
            mod.popSuscetiveis.append(mod.S)
    else:
        while (i < t-1):
            # print(f"{mod.popSuscetiveis[i]} {mod.popInfectados[i]} {mod.popRecuperados[i]}")

            i += 1

            dS = (-mod.r*mod.popSuscetiveis[i - 1]*mod.popInfectados[i - 1])*deltaT
            mod.S = mod.popSuscetiveis[i - 1] + dS

            if (mod.S < 0):
                mod.S = 0 

            dI = (mod.r*mod.popSuscetiveis[i - 1]*mod.popInfectados[i - 1] - mod.alfa*mod.popInfectados[i - 1])*deltaT

            mod.I = mod.popInfectados[i - 1] + dI

            if (mod.I < 0):
                mod.I = 0

            dR = (mod.alfa*mod.popInfectados[i - 1])*deltaT

            mod.R = mod.popRecuperados[i - 1] + dR

            if (mod.R < 0):
                mod.R = 0

            mod.popRecuperados.append(mod.R)
            mod.popInfectados.append(mod.I)
            mod.popSuscetiveis.append(mod.S)
    
    Plot_Geral(mod.popSuscetiveis, mod.popInfectados, mod.popRecuperados)

    print(f"Número máximo de infectados {max(mod.popInfectados)}")
