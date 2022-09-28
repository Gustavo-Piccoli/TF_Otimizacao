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


#Calcula uma solucao inicial para o problema, retorna uma tupla composta pelo valor total e uma lista de listas, onde cada lista interna e um conteiner
#Essa solucao e muito boa no aproveitamento de volumes dos itens, mas nao e muito boa no aproveitamento de valores dos itens
def solucao_inicial(matriz, volume_max_conteiner, numero_conteineres):
    conteineres = []
    controle = list(range (matriz[0][0]))
    for i in range(numero_conteineres): 
        if (len(controle) > 0):
            conteiner = []
            controle_aux = controle.copy()
            while(len(controle_aux) > 0):
                item = random.choice(controle_aux)
                #Esse if faz com que o container fique muito preenchido
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


#Pega a solucao inicial e gera uma solucao vizinha atraves de uma perturbacao aleatoria, que altera o conteudo de um dos containers
def solucao_vizinha(matriz, solucao_original, volume_max_conteiner, numero_conteineres): 
    nova_solucao = solucao_original[1].copy()
    index_container_aleatorio = random.choice(range(numero_conteineres))
    controle = list(range (matriz[0][0]))
    for i in nova_solucao:
        for j in i:
            controle.remove(j)
    for i in (nova_solucao[index_container_aleatorio]):
        controle.append(i)
    novo_conteiner = []
    while(len(controle) > 0):
        item = random.choice(controle)
        if((volume_conteiner_individual(matriz, novo_conteiner) + matriz[-1][item]) <= volume_max_conteiner):
            novo_conteiner.append(item)
        controle.remove(item)
    nova_solucao[index_container_aleatorio] = novo_conteiner
    valor = 0
    for i in nova_solucao:
        valor += valor_conteiner_individual(matriz, i)
    return [valor, nova_solucao]


#Simulated Annealing com o laco de iteracoes e o de temperatura
def simulated_annealing(matriz, volume_conteiner, numero_conteineres, numero_iteracoes, temperatura, fator_resfriamento):
    melhor_inicial = solucao_inicial(matriz, volume_conteiner, numero_conteineres)
    count = 0
    while(temperatura > 1): #Talvez alterar o valor da temperatura final
        for i in range(numero_iteracoes):
            count += 1
            vizinho_candidato = solucao_vizinha(matriz, melhor_inicial, volume_conteiner, numero_conteineres)
            delta = vizinho_candidato[0] - melhor_inicial[0]
            if (delta >= 0):
                melhor_inicial = vizinho_candidato
            else:
                if (random.random() < math.exp(-delta/temperatura)): ##############Arrumar aqui####################
                    melhor_inicial = vizinho_candidato
        temperatura = temperatura * fator_resfriamento
    print(count)
    return melhor_inicial


if  __name__ == "__main__":
    random.seed(1) #Fixa a semente do random para que os resultados sejam sempre os mesmos
    matrizes = cria_matrizes(arquivos)
    numero_conteineres = 10
    volumes_conteineres = volumes_maximos_conteineres(matrizes, numero_conteineres)
    numero_iteracoes = 1000 #Alterar o valor daqui
    temperatura = 100 #Alterar o valor daqui
    fator_resfriamento = 0.9 #Alterar o valor daqui (deve ser entre 0 e 1) 
    s = simulated_annealing(matrizes[0], volumes_conteineres[0], numero_conteineres, numero_iteracoes, temperatura, fator_resfriamento)
    print(s)

'''
##################################INACABADO##################################
#Simulated Annealing com apenas o laco de iteracoes (sem o de temperatura)
def simulated_annealing1(matriz, 
                        volume_conteiner, 
                        numero_conteineres, 
                        numero_iteracoes, 
                        temperatura, 
                        fator_resfriamento):
    melhor_inicial = () #Implementar aqui a funcao de encontrar um melhor aleatorio
    for i in range(numero_iteracoes):
        vizinho_candidato = () #Implementar aqui a funcao de vizinhanca, que pega o melhor_inicial e gera um vizinho atraves de uma perturbacao
        delta = vizinho_candidato - melhor_inicial
        if (delta <= 0):
            melhor_inicial = vizinho_candidato
        else:
            if (random.random() < math.exp(-delta/temperatura)): #Alterar o random daqui
                melhor_inicial = vizinho_candidato
        temperatura = temperatura * fator_resfriamento
    return melhor_inicial

    #Essa linha em comentario em baixo, seria relevante caso quisessemos que o vizinho fosse apenas um iten de um container diferente
    #index_iten_aleatorio = solucao_vizinha[1][index_container_aleatorio].index(random.choice(solucao_vizinha[1][index_container_aleatorio]))
'''