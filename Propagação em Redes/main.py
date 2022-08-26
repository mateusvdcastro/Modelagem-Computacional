# Tempo: Discreto (em dias) (Se discreto não precisa de derivada
# basta o tempo correr em passo 1)
# Estado: Discreto

# 1) Fazer gráfico de Erdos_Renyi (verificar se a rede está toda conexa)
# 2) Barabasi
# 3) Doença contagiosa

import networkx as nx
import matplotlib.pyplot as plt
import random

N = 500 # Número de Vértices
k = 4 # Grau médio de ligações
seed = 1020 # Usado para plotar o mesmo gráfico em lugares diferentes
T = 100 # Tempo máximo de simulação


def redeAleatoria():
    g = nx.Graph() # Construtor

    g.add_nodes_from(range(1, N+1), infectado = 'n', curado = 0, diasDoente = 0) # Adiciona nós

    # Adiciona arestas ao gráfico aleatoriamente 
    for i in g.nodes():
        for j in g.nodes():
            if (i != j):
                
                R = random.random()

                # print(f"Valor de R: {R}")
                comp =  k / (2*N)
                # Check if R<P add the edge to the graph else ignore.
                if (R <= comp):
                    g.add_edge(i, j) # Adiciona uma aresta entre o n 0 e 1, ...
  
    print(nx.degree(g))
    plt.figure(1, figsize=(6, 6))             #definindo o tamanho da figura
    pos= nx.fruchterman_reingold_layout(g)      #definindo o algoritmo do layout
    nx.draw_networkx_nodes(g,pos,node_size=50, node_color = 'b') #plota os nodes
    nx.draw_networkx_edges(g,pos,alpha=0.4)    #plota os ties
    plt.show()
    ############################################################################
    valores_das_arestas = list(dict((nx.degree(g))).values()) # Uma lista da
    # quantidade de arestas que cada vértice está ligado
    count = 0

    for n in valores_das_arestas:

      if (n == 0):
        count += 1

    print("valores sem aresta: ", count)
    print(valores_das_arestas)

    arestas_unicas = list(set(valores_das_arestas)) # Os sets são uma coleção de 
    # itens desordenada, parcialmente imutável e que não podem conter elementos 
    # duplicados.

    arestas_unicas.sort()

    vertices_com_arestas = []

    for i in arestas_unicas:
        vertices_com_arestas.append(valores_das_arestas.count(i)) # count conta
        # a quantidade de ocorrências de um dado valor na lista


    plt.plot(arestas_unicas, vertices_com_arestas)
    plt.xlabel("Arestas")
    plt.ylabel("Numero de Vertices")
    plt.title("Distribuição das Arestas")
    plt.show()

    simulacao(g)



def redeLivre():
    g = nx.Graph() # Construtor

    g.add_nodes_from(range(1, N+1), infectado = 'n', curado = 0, diasDoente = 0) # Adiciona nós

    a = random.randint(1,N)
    b = random.randint(1,N)
    while(a == b):
      b = random.randint(1,N)
    
    g.add_edge(a, b)

    #iniciando o grafo Barabasi
    for i in g.nodes():
        for j in g.nodes():
            if (i != j):
              sum = 0
      
              valores_das_arestas = list(dict((nx.degree(g))).values())
              for z in range(len(valores_das_arestas)):
                  sum = sum + valores_das_arestas[z]

              grau = g.degree[i]

              prob = grau / sum

              R = random.random()

              if (R <= prob):
                  g.add_edge(i, j) # Adiciona uma aresta entre o n 0 e 1, ...

    plt.figure(1, figsize=(6, 6))             #definindo o tamanho da figura
    pos= nx.spring_layout(g)      #definindo o algoritmo do layout
    nx.draw_networkx_nodes(g,pos,node_size=50, node_color = 'g') #plota os nodes
    nx.draw_networkx_edges(g,pos,alpha=0.4)    #plota os ties
    plt.show()
    ############################################################################
    valores_das_arestas = list(dict((nx.degree(g))).values()) # Uma lista da
    # quantidade de arestas que cada vértice está ligado

    count = 0

    for n in valores_das_arestas:

      if (n == 0):
        count += 1

    print("valores sem aresta: ", count)
    print(valores_das_arestas)

    arestas_unicas = list(set(valores_das_arestas))   # Os sets são uma coleção de 
    # itens desordenada, parcialmente imutável e que não podem conter elementos 
    # duplicados.

    arestas_unicas.sort()

    vertices_com_arestas = []

    for i in arestas_unicas:
        vertices_com_arestas.append(valores_das_arestas.count(i)) # count conta
        # a quantidade de ocorrências de um dado valor na lista


    plt.plot(arestas_unicas, vertices_com_arestas)
    plt.xlabel("Arestas")
    plt.ylabel("Numero de Vertices")
    plt.title("Distribuição das Arestas")
    plt.show()

    simulacao(g)


def simulacao(g):

    a = random.randint(1,N)

    g.nodes[a]['infectado'] = 's'

    # print(g.adj)

    doencaProb = 0.15
    curaProb = 0.4
    probMorte = 0.3

    ciclo = 0
    end = 0
    infectados = 0
    recuperados = 0

    quantInfec = []
    quantCuras = []
    individuos = []
    tempoR = []
    retirarNos = []

    while (end == 0 and ciclo <= T):
      # print('1: ',infectados)

      # if (ciclo == 20):
      #   g.remove_node(1)

      for n in g.nodes():
        for m in g.adj[n]:

          R = random.random()

          if(g.nodes[n]['infectado'] == 's'):
            if(g.nodes[m]['infectado'] == 'n'):
              if (R <= doencaProb):
                g.nodes[m]['infectado'] = 's'
      
      for x in g.nodes():
        if(g.nodes[x]['infectado'] == 's'):
          infectados += 1

      # print('2: ',infectados)
      if (ciclo >= 5):
        for r in g.nodes():
          count = 0
          for m in g.adj[r]:
            if(g.nodes[m]['infectado'] == 's'):
              count += 1
          
          R = random.random()
          
          if (count >= len(g.adj[r]) / 2):
            R += 0.2

          if (R <= curaProb and g.nodes[r]['diasDoente'] >= 5):
            g.nodes[r]['diasDoente'] = 0
            g.nodes[r]['infectado'] = 'n'
            g.nodes[r]['curado'] += 1
            recuperados += 1
            infectados -= 1

      #acabou a doença
      if (infectados <= 0):
        end = 1

      # print('3: ',infectados)
      for t in g.nodes():

        if(g.nodes[t]['infectado'] == 's'):
          g.nodes[t]['diasDoente'] += 1

      if (ciclo >= 20):
        for z in g.nodes():
          #morreu
          count = 0
          for m in g.adj[z]:
            if(g.nodes[m]['infectado'] == 'n'):
              count += 1
          
          R = random.random()
          
          if (count >= len(g.adj[z]) / 2):
            R += 0.2

          if (g.nodes[z]['diasDoente'] >= 20 and R <= probMorte):
            retirarNos.append(z)
            infectados -= 1

      for b in retirarNos:
        g.remove_node(b)

      retirarNos = []
      
      quantCuras.append(recuperados)
      individuos.append(g.number_of_nodes())
      quantInfec.append(infectados)
      tempoR.append(ciclo)
      infectados = 0
      recuperados = 0
      ciclo += 1

    print(g.nodes.data())
    print('---------------')
    print(quantInfec)
    print(tempoR)
    print('individuos: ',individuos)
    print('quant dias: ', tempoR[-1])
    print(g.number_of_nodes())
    plt.figure(1, figsize=(12, 6))
    plt.plot(tempoR, individuos, label = 'Indivíduos')
    plt.plot(tempoR, quantCuras, label = 'Quantidade de vezes recuperado')
    plt.plot(tempoR, quantInfec, label = 'Quantidade de infectados')
    plt.xlabel("Tempo")
    plt.ylabel("Quantidade")
    plt.title("Propagação da doença")
    plt.legend()
    plt.show()
        



if __name__ == "__main__":

    redeAleatoria()

    # redeLivre()

    plt.close()

