'''
==========================================================================================================
ARQUIVO............: dsatur.py
DESCRICAO..........: Implementação do algoritmo DSATUR que objetiva extrair a coloração mínima de um grafo
AUTOR..............: Jhonattan Carlos Barbosa Cabral
MODIFICADO EM......: 10/03/2019
===========================================================================================================
'''

class Coloring:
    def __init__(self):
        pass
    
    def coloring_node(self, n, colors, dic):
        colored = False
        color = 0
        while not(colored):
            if color in dic[n[0]][4]:
                color = color+1
            else:
                colored = True
                dic[n[0]][1] = color
                if color >= len(colors):
                    colors[color] = [n[0]]
                else:
                    colors[color].append(n[0])

                for nei in n[1]:
                    dic[nei][4].add(color)

    def remove_node(self, node, dic):
        dic[node][2] = '-' #removendo o vertice de maior grau, pois o mesmo ja obteve coloração
        for key, val in dic.items():
            val[2] = list(filter(lambda a: a != node, val[2])) #desligando o vertice dos seus adjacentes

    def higher_grade(self, lst):     
        max_grade = len(lst[0][1])
        node = (lst[0][0], lst[0][1])
        for l in lst[1:]:
            if len(l[1]) > max_grade:
                max_grade = len(l[1])
                node = (l[0], l[1])
        return node #Retorna o vertice de maior grau e seus vizinhos
    
    def get_amount_of_colors(self, dic):
        return len(dic)

    def higher_saturation_degree(self, dic): #Verifica qual o vertice que possui o maior grau de saturação
        list_of_items = list(dic.items())
        max_saturation = 0
        nodes = []
        for l in list_of_items[1:]:
            if '-' not in l[1][2]:
                if l[1][0] > max_saturation:
                    max_saturation = l[1][0]
        for l in list_of_items:
            if max_saturation == l[1][0]:
                nodes.append(l)
        nodes = list([x for x in nodes if '-' not in x[1][2]])
        if len(nodes)==1:                            #Caso só exista um vertice com grau máximo
            return (True,(nodes[0][0], nodes[0][1][3])) #Retorna o vertice de maior grau de saturação
        else:                                                #Caso contrário
            return (False, [(x[0], x[1][3]) for x in nodes]) #Retorna uma lita de vertices empatados considerando seus graus maximos e seus respsctivos vizinhos

    def neighbors_with_intersec(self, lst, dic):
        neighbors = []
        for key, val in dic.items():
            if key in lst:
                neighbors.append(key)
        return neighbors

    def degree_of_saturation(self, k, dic):
        neighbors = k[1]
        for nei in neighbors:
            dic[nei][0] = len(dic[nei][4])

    def dsatur(self, graph):   
        v = {} #
        for index, val  in enumerate(graph):
            v[int(index)] = [0,-1,val, val, set()]
        colors = {}
        n1 = (graph.index(max(graph, key=len)), max(graph, key=len)) 
        self.coloring_node(n1, colors, v)
        self.degree_of_saturation(n1, v) 
        self.remove_node(n1[0], v)
        
        p = [list(x[2]) for x in v.values() if '-' not in x[2] ]
        
        while(not(len(p)==0)):
            best_node = self.higher_saturation_degree(v)
            
            if not(best_node[0]):
                best_node = self.higher_grade(best_node[1])
            else:
                best_node = best_node[1]
            self.coloring_node(best_node, colors, v)
            self.degree_of_saturation(best_node, v)
            self.remove_node(best_node[0], v)
            p = [list(x[2]) for x in v.values() if '-' not in x[2] ]      
        return (self.get_amount_of_colors(colors), v)