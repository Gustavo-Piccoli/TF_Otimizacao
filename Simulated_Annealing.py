#Bibliotecas a serem importadas
import random
import math
import time


#Nomes dos arquivos
arquivos = ["pcmcdc1.txt", "pcmcdc2.txt", 
            "pcmcdc3.txt", "pcmcdc4.txt",
            "pcmcdc5.txt", "pcmcdc6.txt",
            "pcmcdc7.txt", "pcmcdc8.txt",
            "pcmcdc9.txt", "pcmcdc10.txt"]


#Cria uma lista de listas dos valores numericos de cada linha de cada arquivo
#Essa função foi usada para fazer o processamento dos nossos testes. Ela não é usada no algoritmo a ser rodado pelo terminal de comando.
'''def cria_matrizes(arquivos):
    matrizes = []
    for arquivo in arquivos:
        diretorio = "pcmcdc/" + arquivo
        with open(diretorio) as conteudo_arquivo:
            matriz = []
            for linha in conteudo_arquivo:
                matriz.append(list(map(int, linha.split())))
            matrizes.append(matriz)
    return matrizes
'''


def cria_matriz_individual(arquivo):
    with open(arquivo) as conteudo_arquivo:
        matriz = []
        for linha in conteudo_arquivo:
            matriz.append(list(map(int, linha.split())))
    return matriz


#Calcula os volumes dos conteineres de cada arquivo e retorna eles em uma lista
#Essa função foi usada para fazer o processamento dos nossos testes. Ela não é usada no algoritmo a ser rodado pelo terminal de comando.
'''def volumes_maximos_conteineres(matrizes, numero_conteineres):
    volumes = []
    for matriz in matrizes:
        volumes.append(math.floor((0.8/numero_conteineres) * sum(matriz[-1])))
    return volumes
'''


#Calcula o valor de um conteiner, dada uma lista de itens dentro do conteiner
def valor_dos_itens_dentro_de_um_conteiner(matriz, lista_itens):
    lista_itens.sort()
    valor_total = 0
    for i in range(len(lista_itens)):
        valor_total += matriz[1][lista_itens[i]]
        for j in range(i+1, len(lista_itens)):
            valor_total += matriz[lista_itens[i]+2][lista_itens[j]-lista_itens[i]-1]
    return valor_total


#Calcula o volume dos itens um conteiner, dada uma lista de itens dentro do conteiner
def volume_dos_itens_dentro_de_um_container(matriz, lista_itens):
    lista_itens.sort()
    volume = 0
    for i in lista_itens:
        volume += matriz[-1][i]
    return volume


#Calcula uma solucao inicial para o problema, retorna uma tupla composta pelo valor total e uma lista de listas, onde cada lista interna e um conteiner
def solucao_inicial(matriz, volume_max_conteiner):
    conteineres = []
    controle = list(range (matriz[0][0]))
    for i in range(10): 
        if (len(controle) > 0):
            conteiner = []
            controle_aux = controle.copy()
            while(len(controle_aux) > 0):
                item = random.choice(controle_aux)
                if((volume_dos_itens_dentro_de_um_container(matriz, conteiner) + matriz[-1][item]) <= volume_max_conteiner):
                    conteiner.append(item)
                    controle.remove(item)
                controle_aux.remove(item)
            conteineres.append(conteiner)
        else:
            for j in range(i, 10): #cuidar se o range esta certo
                conteineres.append([])
            break
    valor = 0
    for i in conteineres:
        valor += valor_dos_itens_dentro_de_um_conteiner(matriz, i)
    return [valor, conteineres]


#Pega a solucao inicial e gera uma solucao vizinha atraves de uma perturbacao aleatoria, que altera o conteudo de um dos containers
def solucao_vizinha(matriz, solucao_original, volume_max_conteiner): 
    nova_solucao = solucao_original[1].copy()
    index_container_aleatorio = random.choice(range(10))
    controle = list(range (matriz[0][0]))
    #Esses 2 lacos aninhados geram os novos possiveis itens que podem ser colocados no novo container
    for i in nova_solucao:
        for j in i:
            controle.remove(j)
    for i in (nova_solucao[index_container_aleatorio]):
        controle.append(i)
    novo_conteiner = []
    while(len(controle) > 0):
        item = random.choice(controle)
        if((volume_dos_itens_dentro_de_um_container(matriz, novo_conteiner) + matriz[-1][item]) <= volume_max_conteiner):
            novo_conteiner.append(item)
        controle.remove(item)
    nova_solucao[index_container_aleatorio] = novo_conteiner
    valor = 0
    for i in nova_solucao:
        valor += valor_dos_itens_dentro_de_um_conteiner(matriz, i)
    return [valor, nova_solucao]


#Simulated Annealing com o laco de iteracoes e o de temperatura
'''def simulated_annealing2(matriz, volume_conteiner, numero_iteracoes, temperatura, fator_resfriamento):
    melhor_inicial = solucao_inicial(matriz, volume_conteiner)
    melhor_melhor = melhor_inicial.copy()
    print("Inicial = ", melhor_inicial)
    count = 0
    while(temperatura > 1):
        for i in range(numero_iteracoes):
            count += 1
            vizinho_candidato = solucao_vizinha(matriz, melhor_inicial, volume_conteiner)
            if (vizinho_candidato[0] > melhor_melhor[0]):
                melhor_melhor = vizinho_candidato.copy()
            delta = vizinho_candidato[0] - melhor_inicial[0]
            if (delta >= 0):
                melhor_inicial = vizinho_candidato.copy()
            else:
                if (random.random() < math.exp(delta/temperatura)):
                    melhor_inicial = vizinho_candidato.copy()
        temperatura = temperatura * fator_resfriamento
    print("Melhor_Melhor = ", melhor_melhor)
    return melhor_inicial
'''



#Simulated Annealing com o laco de iteracoes e o de temperatura
def simulated_annealing(arquivo, temperatura_inicial, temperatura_final, fator_resfriamento, numero_iteracoes):
    matriz = cria_matriz_individual(arquivo)
    volume_conteiner = (math.floor((0.8/10) * sum(matriz[-1])))
    melhor_inicial = solucao_inicial(matriz, volume_conteiner)
    melhor_melhor = melhor_inicial.copy()
    print("Inicial = ", melhor_inicial)
    count = 0
    while(temperatura_inicial > temperatura_final):
        for i in range(numero_iteracoes):
            count += 1
            vizinho_candidato = solucao_vizinha(matriz, melhor_inicial, volume_conteiner)
            if (vizinho_candidato[0] > melhor_melhor[0]):
                melhor_melhor = vizinho_candidato.copy()
            delta = vizinho_candidato[0] - melhor_inicial[0]
            if (delta >= 0):
                melhor_inicial = vizinho_candidato.copy()
            else:
                if (random.random() < math.exp(delta/temperatura_inicial)):
                    melhor_inicial = vizinho_candidato.copy()
        temperatura_inicial = temperatura_inicial * fator_resfriamento
    print("\nMelhor_Encontrado = ", melhor_melhor)
    print("\nMelhor_Final = ", melhor_inicial)
    return melhor_inicial



if  __name__ == "__main__":
    
    #Os parametros dos testes finais devem ser:
    #numero_iteracoes = 4000
    #temperatura = 4000
    #fator_resfriamento = 0.9999
    
    random.seed(1) #Fixa a semente do random para que os resultados sejam sempre os mesmos
    #Parametros simulated_annealing()
    #simulated_annealing(nome_do_arquivo, temperatura_inicial, temperatura_final, fator_resfriamento, numero_iteracoes)
    simulated_annealing("pcmcdc1.txt", 100, 1, 0.99, 100)
    
    
    
    
    
    '''
    matrizes = cria_matrizes(arquivos)
    numero_conteineres = 10
    volumes_conteineres = volumes_maximos_conteineres(matrizes, numero_conteineres)
    numero_iteracoes = 4000 #Alterar o valor daqui
    print("###################################################################################################")
    print("numero_iteracoes = ", numero_iteracoes)
    temperatura = 4000 #Alterar o valor daqui
    print("temperatura = ", temperatura)
    fator_resfriamento = 0.9999 #Alterar o valor daqui (deve ser entre 0 e 1)
    print("fator_resfriamento = ", fator_resfriamento, "\n")
    #for i in range(5, 10): #Comandos Gustavo Falta range(8, 10)
    for i in range(8, 10): #Comandos Henrique
        t0 = time.time()
        random.seed(1)
        print("###################################################################################################")
        print("Arquivo",i+1)
        print("\nResultado Final =", simulated_annealing2(matrizes[i], volumes_conteineres[i], numero_conteineres, numero_iteracoes, temperatura, fator_resfriamento), "\n")
        t1 = time.time()
        print("Tempo de execucao = ", t1-t0, "s\n\n\n")
    '''