import networkx as nx
import matplotlib.pyplot as plt
import random


regioes = {
    'Austrália Ocidental': ['Território do Norte', 'Austrália do Sul'],
    'Território do Norte': ['Austrália Ocidental', 'Austrália do Sul', 'Queensland'],
    'Austrália do Sul': ['Austrália Ocidental', 'Território do Norte', 'Queensland', 'Nova Gales do Sul', 'Victoria'],
    'Queensland': ['Território do Norte', 'Austrália do Sul', 'Nova Gales do Sul'],
    'Nova Gales do Sul': ['Austrália do Sul', 'Queensland', 'Victoria'],
    'Victoria': ['Austrália do Sul', 'Nova Gales do Sul'],
    'Tasmânia': [] 
}


grafo = nx.Graph()
for regiao, vizinhos in regioes.items():
    grafo.add_node(regiao)
    for vizinho in vizinhos:
        grafo.add_edge(regiao, vizinho)


posicoes = {
    'Austrália Ocidental': (0, 1),
    'Território do Norte': (1, 2),
    'Austrália do Sul': (1, 1),
    'Queensland': (2, 2),
    'Nova Gales do Sul': (2, 1),
    'Victoria': (1, 0),
    'Tasmânia': (0, 0)  
}


def eh_colorecao_valida(no, cor, coloracao):
    for vizinho in grafo.neighbors(no):
        if vizinho in coloracao and coloracao[vizinho] == cor:
            return False
    return True


def colorir_mapa(grafo):
    coloracao = {}
    cores = ['red', 'green', 'blue', 'yellow'] 

    for no in grafo.nodes():
        cores_disponiveis = cores.copy()
        random.shuffle(cores_disponiveis) 

        for cor in cores_disponiveis:
            if eh_colorecao_valida(no, cor, coloracao):
                coloracao[no] = cor
                break
    return coloracao


coloracao = colorir_mapa(grafo)


nx.draw(grafo, pos=posicoes, with_labels=True, node_color=[coloracao[no] for no in grafo.nodes()], node_size=2000)
plt.title('Coloração do Mapa das Regiões da Austrália')
plt.show()
