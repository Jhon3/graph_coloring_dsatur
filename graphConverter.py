'''
============================================================================================================
ARQUIVO............: graphConverter.py
DESCRICAO..........: Converte os arquivos dos casos de teste para um grafo no formato de lista de adjacência
AUTOR..............: Jhonattan Carlos Barbosa Cabral
MODIFICADO EM......: 10/03/2019
=============================================================================================================
'''

from dsatur import Coloring
import re

class Converter:
    def __init__(self):
        pass

    def convert(self, file):
        lines = []
        
        with open(file) as f:
            lines = f.read().splitlines()
        inf = lines[0].split(' ')
        graph = [[] for x in range(int(inf[2]))]
        lines = [re.sub('e', '', x) for x in lines if x.find('p')==-1]
        lines = [x[1:].split(' ') for x in lines]
        for l in lines:
            if (int(l[1])-1 not in graph[int(l[0])-1]) and (int(l[0])-1 not in graph[int(l[1])-1]):
                graph[int(l[0])-1].append(int(l[1])-1)
                graph[int(l[1])-1].append(int(l[0])-1)
        return (inf, graph)
