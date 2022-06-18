import numpy as np
import matplotlib.pyplot as plt
import random as rd

# N(t) número de indivíduos de uma população em função do tempo
# Considera que a população cresce a uma razão Alpha na ausência de fatores limitantes
# P é a ppulação de predadores

i = 0
t = 5000  # tempo
k = 200  # representa a capacidade de suporte do ambiente (saturação)
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

        ax[0, 0].plot(T, rato, 'b', label='Ratos')
        ax[0, 0].plot(T, coruja, 'm', label='Coruja')
        ax[0, 0].set_xlabel('Tempo (t)')
        ax[0, 0].set_ylabel('Número de indivíduos')
        ax[0, 0].legend()
        ax[0, 0].set_title('População de Ratos e Corujas')

        ax[0, 1].plot(T, plantas, 'r', label='Plantas')
        ax[0, 1].plot(T, rato, 'b', label='Ratos')
        ax[0, 1].plot(T, vacas, 'y', label='Vacas')
        ax[0, 1].plot(T, joaninhas, 'c', label='Joaninhas')
        ax[0, 1].plot(T, coruja, 'm', label='Corujas')
        ax[0, 1].set_xlabel('Tempo (t)')
        ax[0, 1].set_ylabel('Número de indivíduos')
        ax[0, 1].legend(loc = 'upper right', fontsize=6)
        ax[0, 1].set_title('Populações que dependem das plantas')

        ax[1, 0].plot(T, rato, 'b', label='Ratos')
        ax[1, 0].plot(T, oncas, 'g', label='Oncas')
        ax[1, 0].plot(T, vacas, 'y', label='Vacas')
        ax[1, 0].set_xlabel('Tempo (t)')
        ax[1, 0].set_ylabel('Número de indivíduos')
        ax[1, 0].legend(loc = 'upper right', fontsize=6)
        ax[1, 0].set_title('População de Ratos, Oncas e Vacas')

        ax[1, 1].plot(T, plantas, 'r', label='Plantas')
        ax[1, 1].plot(T, vacas, 'y', label='Vacas')
        ax[1, 1].set_xlabel('Tempo (t)')
        ax[1, 1].set_ylabel('Número de indivíduos')
        ax[1, 1].legend()
        ax[1, 1].set_title('População de Plantas e Vacas')
        # plt.subplots_adjust(wspace=1, hspace=1, top=1.2, right=0.9, left=0.1)
        plt.show()

    def Volterra(self, plantas=None, rato=None, oncas=None, vacas=None, joaninhas=None, coruja=None):
        """
        Plota o gráfico de LOTKA-VOLTERRA

        """

        plt.plot(plantas, vacas, 'r', label='Plantas x Vacas')
        plt.plot(oncas, rato, label='Oncas X Ratos')
        plt.plot(oncas, vacas, label='Oncas X Vacas')
        plt.plot(joaninhas, plantas, label='Joaninhas X Plantas')
        plt.plot(joaninhas, coruja, label='Joaninhas X Corujas')
        plt.xlabel('Espécies')
        plt.ylabel('Espécies')
        plt.title("Gráfico de Lotka-Volterra")
        plt.legend()

    def DoencaRato(self, ratos):
        Pop = []
        Tempo = []
        for i in range(5000):
            PopR = ratos[i] * - ((i/50)**2)+5000
            i += 1
            Pop.append(PopR)
            Tempo.append(i)
            if (PopR < 0):
                break

        plt.plot(Tempo, Pop, label='População de Ratos doentes')



if __name__ == "__main__":

    # Cria o ambiente planta e seus coeficientes

    # Simulção 1: 10 0.1 0.1 0.2
    # Simulção 2: 5  0.7 0.1 0.3
    # Simulção 3:
    # Simulção 4:
    # Simulção 5:

    planta = {
        "planta": 5,
        "vaca": 0.7,
        "joaninha": 0.1,
        "rato": 0.3,
    }

    plantas = Especie(N=50, p=[planta.get("planta"), planta.get(
        "vaca"), planta.get("joaninha"), planta.get("rato")], k=50)

    # Cria a espécie dos ratos e seus coeficientes

    # Simulção 1: 1.75 0.175 0,9 0.9
    # Simulção 2: 0.1  2     0.3 0.6
    # Simulção 3:
    # Simulção 4:
    # Simulção 5:

    ratos = {
        "rato": 0.1,
        "planta": 2,
        "onça": 0.3,
        "coruja": 0.6,
    }

    rato = Especie(N=30, p=[ratos.get("rato"), ratos.get(
        "planta"), ratos.get("onça"), ratos.get("coruja")], k=30)

    # Cria a espécie coelhos e seus coeficientes

    # Simulção 1: 8.5 0.1 0.1
    # Simulção 2: 0.8 0.1 0.1
    # Simulção 3: 0.8 0.5 0.1
    # Simulção 4:
    # Simulção 5:

    onca = {
        "onca": 0.8,
        "vaca": 0.5,
        "rato": 0.1,
    }

    oncas = Especie(N=15, p=[onca.get("onca"), onca.get(
        "vaca"), onca.get("rato")], k=15)

    # Cria a espécie das vacas e seus coeficientes

    # Simulção 1: 0.8 0.5 0.5
    # Simulção 2: 0.8 0.9 0.9
    # Simulção 3: 0.8 0.2 0.9
    # Simulção 4: 0.8 0.3 0.9  # populações de vacas e plantas desimadas
    # Simulção 5:

    vaca = {
        "vaca": 0.8,
        "planta": 2,
        "onça": 0.9,
    }

    vacas = Especie(N=40, p=[vaca.get("vaca"), vaca.get(
        "planta"), vaca.get("onça")], k=40)

    # Cria a espécie joaninha e seus coeficientes

    # Simulção 1: 2.25 0.95 0.6
    # Simulção 2: 0.4  0.95 0.5
    # Simulção 3:
    # Simulção 4:
    # Simulção 5:

    joaninhas = {
        "joaninha": 0.4,
        "planta": 0.95,
        "coruja": 0.5,
    }

    joaninha = Especie(N=35, p=[joaninhas.get("joaninha"), joaninhas.get(
        "planta"), joaninhas.get("coruja")], k=35)

    # Cria a espécie Passáro e seus coeficientes

    # Simulção 1: 8.5  0.5  0.5
    # Simulção 2: 0.4  0.2  0.7
    # Simulção 3:
    # Simulção 4:
    # Simulção 5:

    corujas = {
        "coruja": 0.4,
        "joaninha": 0.2,
        "rato": 0.7,
    }

    coruja = Especie(N=30, p=[corujas.get("coruja"), corujas.get(
        "joaninha"), corujas.get("rato")], k=30)

    while(i < t-1):
        i += 1

        plantas.N = plantas.vetor[i - 1] + plantas.vetor[i - 1] * (plantas.p[0] * (1 - plantas.vetor[i - 1] / plantas.k) -
                                                                   plantas.p[1]*vacas.vetor[i - 1] - plantas.p[2]*joaninha.vetor[i - 1] - plantas.p[3] * rato.vetor[i - 1]) * deltaT

        if (plantas.N < 0):
            plantas.N = 0

        plantas.vetor.append(plantas.N)

        rato.N = rato.vetor[i-1] + rato.vetor[i-1] * (rato.p[1] * plantas.vetor[i - 1] -
                                                      rato.p[2] * oncas.vetor[i - 1] - rato.p[3]*coruja.vetor[i - 1] - rato.p[0]) * deltaT

        if (rato.N < 0):
            rato.N = 0

        rato.vetor.append(rato.N)

        oncas.N = oncas.vetor[i-1] + oncas.vetor[i-1] * (
            oncas.p[1] * vacas.vetor[i - 1] + oncas.p[2] * rato.vetor[i - 1] - oncas.p[0]) * deltaT

        if (oncas.N < 0):
            oncas.N = 0

        oncas.vetor.append(oncas.N)

        vacas.N = vacas.vetor[i-1] + vacas.vetor[i-1] * (
            vacas.p[1] * plantas.vetor[i - 1] - vacas.p[2]*oncas.vetor[i - 1] - vacas.p[0]) * deltaT

        if (vacas.N < 0):
            vacas.N = 0

        vacas.vetor.append(vacas.N)

        joaninha.N = joaninha.vetor[i-1] + joaninha.vetor[i-1] * (
            joaninha.p[1] * plantas.vetor[i - 1] - joaninha.p[2] * coruja.vetor[i - 1] - joaninha.p[0]) * deltaT

        if (joaninha.N < 0):
            joaninha.N = 0

        joaninha.vetor.append(joaninha.N)

        coruja.N = coruja.vetor[i-1] + coruja.vetor[i-1] * (
            coruja.p[1] * joaninha.vetor[i - 1] + coruja.p[2]*rato.vetor[i - 1] - coruja.p[0]) * deltaT

        if (coruja.N < 0):
            coruja.N = 0

        coruja.vetor.append(coruja.N)

    graficos = Plots()

    graficos.individuosPeloTempo(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor,
                                 vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)

    graficos.PlotGeral(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor,
                       vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)

    graficos.Volterra(plantas=plantas.vetor, rato=rato.vetor, oncas=oncas.vetor,
                      vacas=vacas.vetor, joaninhas=joaninha.vetor, coruja=coruja.vetor)

    # graficos.DoencaRato(ratos=vacas.vetor)

    plt.show()
    plt.close()
