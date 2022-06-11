import numpy as np
import matplotlib.pyplot as plt
import random as rd

# N(t) número de indivíduos de uma população em função do tempo
# Considera que a população cresce a uma razão Alpha na ausência de fatores limitantes
# P é a ppulação de predadores

print("Hello world")

i = 0
t = 5000 # tempo
k = 200 # representa a capacidade de suporte do ambiente (saturação)
deltaT = 0.01
T = np.arange(0, t * 0.01, deltaT)     

class Especie:
    def __init__(self, N, p=None, k=None):
        self.N = N
        self.p = p
        self.k = k
        self.vetor = [N]

# class Plots:
#     def __init__(self, grama=None, coelho=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
#         self.grama = grama
#         self.coelho = coelho
#         self.oncas = oncas
#         self.vacas = vacas
#         self.joaninhas = joaninhas
#         self.coruja = coruja
    
#     def PlotGeral(self, grama=None, predador=None, presas=None):
#         plt.plot(T, grama, label='Grama')
#         plt.plot(T, predador, label='Predador')
#         plt.plot(T, presas, label='Presas')
#         plt.legend()
#         plt.show()

if __name__ == "__main__":

    # Cria os coeficientes do ambiente grama

    grama = Especie(N=15, p=[10, 0.1, 0.1, 0.2], k=100)

    # Cria a espécie coelhos e seus coeficientes

    coelho = Especie(N=23, p=[1.75, 0.175, 0.9], k=50)

    # Cria a espécie coelhos e seus coeficientes

    oncas = Especie(N=15, p=[8.5, 0.1, 0.1], k=50)

    # Cria a espécie das vacas e seus coeficientes

    vacas = Especie(N=15, p=[0.8, 0.9, 0.15], k=50)

    # Cria a espécie joaninha e seus coeficientes

    joaninha = Especie(N=50, p=[2.25, 0.2, 0.09], k=50)

    # Cria a espécie Passáro e seus coeficientes

    coruja = Especie(N=100, p=[8.5, 0.01, 0.1], k=50)

    while(i < t-1):
        i += 1

        grama.N = grama.vetor[i - 1] + grama.vetor[i - 1] * (grama.p[0] * (1 - grama.vetor[i - 1] / grama.k) - grama.p[1]*coelho.vetor[i - 1] - grama.p[2]*joaninha.vetor[i - 1] - grama.p[3]*vacas.vetor[i - 1]) * deltaT

        if (grama.N < 0):
            grama.N = 0

        grama.vetor.append(grama.N)

        coelho.N = coelho.vetor[i-1] + coelho.vetor[i-1] * (coelho.p[1] * grama.vetor[i - 1] - coelho.p[2] * oncas.vetor[i - 1] - coelho.p[0]) * deltaT

        if (coelho.N < 0):
            coelho.N = 0

        coelho.vetor.append(coelho.N)

        oncas.N = oncas.vetor[i-1] + oncas.vetor[i-1] * (oncas.p[1] * coelho.vetor[i - 1] + oncas.p[2]* vacas.vetor[i - 1] - oncas.p[0]) * deltaT

        if (oncas.N < 0):
            oncas.N = 0
        
        oncas.vetor.append(oncas.N)

        vacas.N = vacas.vetor[i-1] + vacas.vetor[i-1] * (vacas.p[1] * grama.vetor[i - 1] - vacas.p[2]*oncas.vetor[i - 1] - vacas.p[0]) * deltaT

        if (vacas.N < 0):
            vacas.N = 0

        vacas.vetor.append(vacas.N)

        joaninha.N = joaninha.vetor[i-1] + joaninha.vetor[i-1] * (joaninha.p[1] * grama.vetor[i - 1] - joaninha.p[2] * coruja.vetor[i - 1] - joaninha.p[0]) * deltaT

        if (joaninha.N < 0):
            joaninha.N = 0
        
        joaninha.vetor.append(joaninha.N)

        coruja.N = coruja.vetor[i-1] + coruja.vetor[i-1] * (coruja.p[1] * joaninha.vetor[i - 1] - coruja.p[0]) * deltaT

        if (coruja.N < 0):
            coruja.N = 0
        
        coruja.vetor.append(coruja.N)

    # Plota o gráfico de cada indivíduo em função do tempo
    plt.plot(T, grama.vetor, label='Grama')
    plt.plot(T, coelho.vetor, label='Coelho')
    plt.plot(T, oncas.vetor, label='Oncas')
    plt.plot(T, vacas.vetor, label='Vacas')
    plt.plot(T, joaninha.vetor, label='Joaninhas')
    plt.plot(T, coruja.vetor, label='Corujas')
    plt.xlabel('Tempo')
    plt.ylabel('Espécies')
    plt.title("Plot por Espécies")
    plt.legend()

    # # Plota o gráfico de LOTKA-VOLTERRA
    # plt.plot(joaninha.vetor, grama.vetor, label='--')
    # plt.plot(oncas.vetor, coelho.vetor, label='--')
    # plt.plot(oncas.vetor, vacas.vetor, label='--')
    # plt.plot(grama.vetor, joaninha.vetor, label='--')
    # plt.plot(joaninha.vetor, coruja.vetor, label='--')
    # plt.xlabel('Espécies')
    # plt.ylabel('Espécies')
    # plt.title("Gráfico de Lotka-Volterra")
    # plt.legend()

    plt.show()
