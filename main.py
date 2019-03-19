'''
==========================================================================================================
ARQUIVO............: main.py
DESCRICAO..........: Gerenciador de arquivos, para melhor manipulação do projeto
AUTOR..............: Jhonattan Carlos Barbosa Cabral
MODIFICADO EM......: 10/03/2019
===========================================================================================================
'''


from experiment import Experiment

print("1 - Run for a specific case of test:")
print("2 - Run for all case of test and get the result:")

pressed = input()
if pressed.isdigit() and int(pressed) < 3:
    experiment = Experiment()
    if int(pressed) is 1:
        print("Please, put the name of case of test:") #Espera-se algo como --> test_??
        filename = input()
        result = experiment.runTest(0, filename)
        print(result)  #Formato da impressão --> caso de teste | coloração ótima | resultado do algoritmo | tempo
    else:
        print("Inicio do processamento")
        experiment.runTest(1, '')
        print("Resultados salvos em result_of_test.txt.") #Formato de saida --> caso de teste | vertices | arestas | coloração ótima | resultado do algoritmo | tempo
else:
    print("Invalid input, please repeat the program!")
