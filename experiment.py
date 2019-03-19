'''
==========================================================================================================
ARQUIVO............: experiment.py
DESCRICAO..........: Arquivo responsável por rodar os casos de teste utilizando o DSATUR
AUTOR..............: Jhonattan Carlos Barbosa Cabral
MODIFICADO EM......: 10/03/2019
===========================================================================================================
'''

from dsatur import Coloring
from graphConverter import Converter
import re
import time
import numpy as np

class Experiment:
    def __init__(self):
        pass

    def runTest(self, choice, fileName):
        c = Converter()
        d = Coloring()

        if(not(choice)):
            graph = c.convert('./test_cases/'+ fileName +'.col')
            optmialColoring = int(graph[0][3])

            time_init = time.time()
            result_of_dsatur = d.dsatur(graph[1])
            end_time = time.time()
            time_total = end_time - time_init
            result_of_dsatur_coloring = result_of_dsatur[0]
            
            return (fileName, optmialColoring, result_of_dsatur_coloring, time_total)

        else:
            result_of_test = np.zeros((50, 6))
            for x in range(30):
                converted = c.convert('./test_cases/test_'+str(x)+'.col')

                result_of_test[x,0] = str(x)  #Alocando o caso de teste analisado
                result_of_test[x,1] = converted[0][1] #Quantidade de vertices
                result_of_test[x,2] = converted[0][2] #Quantidade de arestas
                result_of_test[x,3] = converted[0][3] #Coloração ótima
                
                time_init = time.time()
                result_of_dsatur = d.dsatur(converted[1])
                end_time = time.time()

                time_total = end_time - time_init
                result_of_test[x,4] = result_of_dsatur[0]
                result_of_test[x,5] = time_total
                print("test_" + str(x) + ".col")
                np.savetxt('./result/result_of_test.txt', result_of_test, fmt='%f')
    