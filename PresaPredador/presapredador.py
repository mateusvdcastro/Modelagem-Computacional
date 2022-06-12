import numpy as np
import matplotlib.pyplot as plt
import random as rd

# N(t) número de indivíduos de uma população em função do tempo
# Considera que a população cresce a uma razão Alpha na ausência de fatores limitantes
# P é a ppulação de predadores

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

class Plots:
    def __init__(self, plantas=None, rato=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
        self.plantas = plantas
        self.rato = rato
        self.oncas = oncas
        self.vacas = vacas
        self.joaninhas = joaninhas
        self.coruja = coruja

    def individuosPeloTempo(self, plantas=None, rato=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
        """
        Plota o gráfico de N(t)
        """
        # Plota o gráfico de cada indivíduo em função do tempo
        plt.plot(T, plantas, label='Plantas')
        plt.plot(T, rato, label='Ratos')
        plt.plot(T, oncas, label='Onças')
        plt.plot(T, vacas, label='Vacas')
        plt.plot(T, joaninhas, label='Joaninhas')
        plt.plot(T, coruja, label='Corujas')
        plt.xlabel('Tempo')
        plt.ylabel('Espécies')
        plt.title("Plot por Espécies")
        plt.legend()

    
    def PlotGeral(self, plantas=None, rato=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
        fig, ax = plt.subplots(2, 2)
        ax[0, 0].plot(T, plantas, 'r', label='Grama')
        ax[0, 0].plot(T, rato, 'b', label='Ratos')
        ax[0, 0].plot(T, oncas, 'g', label='Oncas')
        ax[0, 0].plot(T, vacas, 'y', label='Vacas')
        ax[0, 0].plot(T, joaninhas, 'c', label='Joaninhas')
        ax[0, 0].plot(T, coruja, 'm', label='Coruja')
        ax[0, 0].set_xlabel('Tempo (dias)')
        ax[0, 0].set_ylabel('Número de indivíduos')
        ax[0, 0].legend()
        ax[0, 0].set_title('População')

        ax[0, 1].plot(T, plantas, 'r', label='Grama')
        ax[0, 1].plot(T, rato, 'b', label='Ratos')
        ax[0, 1].plot(T, oncas, 'g', label='Oncas')
        ax[0, 1].plot(T, vacas, 'y', label='Vacas')
        ax[0, 1].plot(T, joaninhas, 'c', label='Joaninhas')
        ax[0, 1].plot(T, coruja, 'm', label='Coruja')
        ax[0, 1].set_xlabel('Tempo (dias)')
        ax[0, 1].set_ylabel('Número de indivíduos')
        ax[0, 1].legend()
        ax[0, 1].set_title('População')

        ax[1, 0].plot(T, plantas, 'r', label='Grama')
        ax[1, 0].plot(T, rato, 'b', label='Ratos')
        ax[1, 0].plot(T, oncas, 'g', label='Oncas')
        ax[1, 0].plot(T, vacas, 'y', label='Vacas')
        ax[1, 0].plot(T, joaninhas, 'c', label='Joaninhas')
        ax[1, 0].plot(T, coruja, 'm', label='Coruja')
        ax[1, 0].set_xlabel('Tempo (dias)')
        ax[1, 0].set_ylabel('Número de indivíduos')
        ax[1, 0].legend()
        ax[1, 0].set_title('População')

        ax[1, 1].plot(T, plantas, 'r', label='Grama')
        ax[1, 1].plot(T, rato, 'b', label='Ratos')
        ax[1, 1].plot(T, oncas, 'g', label='Oncas')
        ax[1, 1].plot(T, vacas, 'y', label='Vacas')
        ax[1, 1].plot(T, joaninhas, 'c', label='Joaninhas')
        ax[1, 1].plot(T, coruja, 'm', label='Coruja')
        ax[1, 1].set_xlabel('Tempo (dias)')
        ax[1, 1].set_ylabel('Número de indivíduos')
        ax[1, 1].legend()
        ax[1, 1].set_title('População')
        plt.legend()
        plt.show()
    
    def Volterra(self, plantas=None, rato=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
        """
        Plota o gráfico de LOTKA-VOLTERRA

        """
        
        plt.plot(joaninhas, plantas, label='Joaninhas X Plantas')
        plt.plot(oncas, rato, label='Oncas X Ratos')
        plt.plot(oncas, vacas, label='Oncas X Vacas')
        plt.plot(plantas, joaninhas, label='Plantas X Joaninhas')
        plt.plot(joaninhas, coruja, label='Joaninhas X Corujas')
        plt.xlabel('Espécies')
        plt.ylabel('Espécies')
        plt.title("Gráfico de Lotka-Volterra")
        plt.legend()


if __name__ == "__main__":

    # Cria o ambiente planta e seus coeficientes

    plantas = Especie(N=50, p=[10, 0.1, 0.1, 0.2], k=50)

    # Cria a espécie dos ratos e seus coeficientes

    rato = Especie(N=30, p=[1.75, 0.175, 0.9, 0.9], k=30)

    # Cria a espécie coelhos e seus coeficientes

    oncas = Especie(N=15, p=[8.5, 0.1, 0.1], k=15)

    # Cria a espécie das vacas e seus coeficientes

    vacas = Especie(N=40, p=[0.8, 0.5, 0.5], k=40)

    # Cria a espécie joaninha e seus coeficientes

    joaninha = Especie(N=35, p=[2.25, 0.95, 0.6], k=35)

    # Cria a espécie Passáro e seus coeficientes

    coruja = Especie(N=30, p=[8.5, 0.5, 0.5], k=30)

    while(i < t-1):
        i += 1

        plantas.N = plantas.vetor[i - 1] + plantas.vetor[i - 1] * (plantas.p[0] * (1 - plantas.vetor[i - 1] / plantas.k) - plantas.p[1]*vacas.vetor[i - 1] - plantas.p[2]*joaninha.vetor[i - 1] - plantas.p[3]*rato.vetor[i - 1]) * deltaT

        if (plantas.N < 0):
            plantas.N = 0

        plantas.vetor.append(plantas.N)

        rato.N = rato.vetor[i-1] + rato.vetor[i-1] * (rato.p[1] * plantas.vetor[i - 1] - rato.p[2] * oncas.vetor[i - 1] - rato.p[3]*coruja.vetor[i - 1] - rato.p[0]) * deltaT

        if (rato.N < 0):
            rato.N = 0

        rato.vetor.append(rato.N)

        oncas.N = oncas.vetor[i-1] + oncas.vetor[i-1] * (oncas.p[1] * vacas.vetor[i - 1] + oncas.p[2]* rato.vetor[i - 1] - oncas.p[0]) * deltaT

        if (oncas.N < 0):
            oncas.N = 0
        
        oncas.vetor.append(oncas.N)

        vacas.N = vacas.vetor[i-1] + vacas.vetor[i-1] * (vacas.p[1] * plantas.vetor[i - 1] - vacas.p[2]*oncas.vetor[i - 1] - vacas.p[0]) * deltaT

        if (vacas.N < 0):
            vacas.N = 0

        vacas.vetor.append(vacas.N)

        joaninha.N = joaninha.vetor[i-1] + joaninha.vetor[i-1] * (joaninha.p[1] * plantas.vetor[i - 1] - joaninha.p[2] * coruja.vetor[i - 1] - joaninha.p[0]) * deltaT

        if (joaninha.N < 0):
            joaninha.N = 0
        
        joaninha.vetor.append(joaninha.N)

        coruja.N = coruja.vetor[i-1] + coruja.vetor[i-1] * (coruja.p[1] * joaninha.vetor[i - 1] + coruja.p[2]*rato.vetor[i - 1] - coruja.p[0]) * deltaT

        if (coruja.N < 0):
            coruja.N = 0
        
        coruja.vetor.append(coruja.N)

    graficos = Plots()

    graficos.individuosPeloTempo(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor, vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)
   
    graficos.PlotGeral(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor, vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)

    graficos.Volterra(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor, vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)

    plt.show()
