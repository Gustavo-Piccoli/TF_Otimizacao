
#Nomes dos arquivos
arquivos = ["pcmcdc1.txt", "pcmcdc2.txt", 
            "pcmcdc3.txt", "pcmcdc4.txt",
            "pcmcdc5.txt", "pcmcdc6.txt",
            "pcmcdc7.txt", "pcmcdc8.txt",
            "pcmcdc9.txt", "pcmcdc10.txt"]

#Cria uma lista de listas dos valores numericos de cada linha de cada arquivo
matrizes = []
for arquivo in arquivos:
    with open(arquivo) as conteudo_arquivo:
        matriz = []
        for linha in conteudo_arquivo:
            matriz.append(list(map(int, linha.split())))
        matrizes.append(matriz)

#Cada elemento de matrizes possui os valores numericos de cada linha de um arquivo
print(matrizes[0])

