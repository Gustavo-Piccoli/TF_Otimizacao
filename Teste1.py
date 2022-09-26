#Bibliotecas a serem importadas
import random
import math


#Nomes dos arquivos
arquivos = ["pcmcdc1.txt", "pcmcdc2.txt", 
            "pcmcdc3.txt", "pcmcdc4.txt",
            "pcmcdc5.txt", "pcmcdc6.txt",
            "pcmcdc7.txt", "pcmcdc8.txt",
            "pcmcdc9.txt", "pcmcdc10.txt"]


#Cria uma lista de listas dos valores numericos de cada linha de cada arquivo
def cria_matrizes(arquivos):
    matrizes = []
    for arquivo in arquivos:
        with open(arquivo) as conteudo_arquivo:
            matriz = []
            for linha in conteudo_arquivo:
                matriz.append(list(map(int, linha.split())))
            matrizes.append(matriz)
    return matrizes


#Calcula os volumes dos containeres de cada arquivo e retorna eles em uma lista
def calcula_volumes(matrizes, numero_containers):
    volumes = list()
    for matriz in matrizes:
        volumes.append(math.floor((0.8/numero_containers) * sum(matriz[-1]))) #MUDAR AQUI
    return volumes


#Calcula o valor de um container, dada uma lista de itens dentro do container
def calcula_valor_container(matriz, lista_itens):
    lista_itens.sort() #ordena os indices dos itens da lista crescentemente, caso ja nao esteja ordenada
    valor_total = 0
    for i in range(len(lista_itens)):
        valor_total += matriz[1][lista[i]]
        for j in range(i+1, len(lista_itens)):
            valor_total += matriz[lista_itens[i]+2][lista_itens[j]-lista_itens[i]-1]
    return valor_total





##################################INACABADO##################################
#Simulated Annealing com apenas o laço de iterações (sem o de temperatura)
def simulated_annealing1(matriz, 
                        volume_container, 
                        numero_containers, 
                        numero_iteracoes, 
                        temperatura, 
                        fator_resfriamento):
    melhor_inicial = () #Implementar aqui a função de encontrar um melhor aleatório
    for i in range(numero_iteracoes):
        vizinho_candidato = () #Implementar aqui a função de vizinhança, que pega o melhor_inicial e gera um vizinho através de uma perturbação
        delta = vizinho_candidato - melhor_inicial
        if (delta <= 0):
            melhor_inicial = vizinho_candidato
        else:
            if (random.random() < math.exp(-delta/temperatura)): #Alterar o random daqui
                melhor_inicial = vizinho_candidato
        temperatura = temperatura * fator_resfriamento
    return melhor_inicial

##################################INACABADO##################################
#Simulated Annealing com o laço de iterações e o de temperatura
def simulated_annealing2(matriz,
                        volume_container,
                        numero_containers,
                        numero_iteracoes,
                        temperatura,
                        fator_resfriamento):
    melhor_inicial = () #Implementar aqui a função de encontrar um melhor aleatório
    while(temperatura > 0): #Talvez alterar o valor da temperatura final
        for i in range(numero_iteracoes):
            vizinho_candidato = () #Implementar aqui a função de vizinhança, que pega o melhor_inicial e gera um vizinho através de uma perturbação aleatória
            delta = vizinho_candidato - melhor_inicial
            if (delta <= 0):
                melhor_inicial = vizinho_candidato
            else:
                if (random.random() < math.exp(-delta/temperatura)): #Alterar o random daqui
                    melhor_inicial = vizinho_candidato
        temperatura = temperatura * fator_resfriamento
    return melhor_inicial   



    
 

if  __name__ == "__main__":
    random.seed(1) #Fixa a semente do random para que os resultados sejam sempre os mesmos
    
    #matrizes = cria_matrizes(arquivos)
    #numero_containers = 10 #numero de containers

    matrizes = cria_matrizes(["mini_teste.txt"]) ################# APAGAR_AQUI #################
    numero_containers = 3 ################# APAGAR_AQUI #################

    volumes_containers = calcula_volumes(matrizes, numero_containers)
    numero_iteracoes = 1000
    temperatura = 1000 
    fator_resfriamento = 0.9 #deve ser entre 0 e 1
    #for i in range(len(matrizes)):
    #    simulated_annealing2(matrizes[i], volumes_containers[i], numero_containers, numero_iteracoes, temperatura, fator_resfriamento)

