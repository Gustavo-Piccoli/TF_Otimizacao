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


#Calcula os volumes dos conteineres de cada arquivo e retorna eles em uma lista
def volumes_maximos_conteineres(matrizes, numero_conteineres):
    volumes = []
    for matriz in matrizes:
        volumes.append(math.floor((0.8/numero_conteineres) * sum(matriz[-1])))
    return volumes


#Calcula o valor de um conteiner, dada uma lista de itens dentro do conteiner
def valor_conteiner_individual(matriz, lista_itens):
    lista_itens.sort()
    valor_total = 0
    for i in range(len(lista_itens)):
        valor_total += matriz[1][lista_itens[i]]
        for j in range(i+1, len(lista_itens)):
            valor_total += matriz[lista_itens[i]+2][lista_itens[j]-lista_itens[i]-1]
    return valor_total


#Calcula o volume dos itens um conteiner, dada uma lista de itens dentro do conteiner
def volume_conteiner_individual(matriz, lista_itens):
    lista_itens.sort()
    volume = 0
    for i in lista_itens:
        volume += matriz[-1][i]
    return volume


#Calcula uma solução inicial para o problema, retorna uma tupla composta pelo valor total e uma lista de listas, onde cada lista interna é um conteiner
#Essa solução é muito boa no aproveitamento de volumes dos itens, mas não é muito boa no aproveitamento de valores dos itens
def solucao_inicial(matriz, volume_max_conteiner, numero_conteineres):
    conteineres = []
    controle = list(range (matriz[0][0]))
    for i in range(numero_conteineres): #Essa funcao poderia ser mais eficiente principalmente para arquivos com poucos itens
        if (len(controle) > 0):
            conteiner = []
            controle_aux = controle.copy()
            while(len(controle_aux) > 0):
                item = random.choice(controle_aux)
                if((volume_conteiner_individual(matriz, conteiner) + matriz[-1][item]) <= volume_max_conteiner):
                    conteiner.append(item)
                    controle.remove(item)
                controle_aux.remove(item)
            conteineres.append(conteiner)
        else:
            for j in range(i, numero_conteineres): #cuidar se o range esta certo
                conteineres.append([])
            break
    valor = 0
    for i in conteineres:
        valor += valor_conteiner_individual(matriz, i)
    return [valor, conteineres]


##################################INACABADO##################################
#Simulated Annealing com apenas o laço de iterações (sem o de temperatura)
'''
def simulated_annealing1(matriz, 
                        volume_conteiner, 
                        numero_conteineres, 
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
'''


##################################INACABADO##################################
#Simulated Annealing com o laço de iterações e o de temperatura
def simulated_annealing(matriz,
                        volume_conteiner,
                        numero_conteineres,
                        numero_iteracoes,
                        temperatura,
                        fator_resfriamento):
    melhor_inicial = solucao_inicial(matriz, volume_conteiner, numero_conteineres)
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
    
    matrizes = cria_matrizes(arquivos)
    numero_conteineres = 10
    volumes_conteineres = volumes_maximos_conteineres(matrizes, numero_conteineres)
    numero_iteracoes = 100
    temperatura = 100
    fator_resfriamento = 0.9 #deve ser entre 0 e 1

    #s = simulated_annealing(matrizes[0], volumes_conteineres[0], numero_conteineres, numero_iteracoes, temperatura, fator_resfriamento)
