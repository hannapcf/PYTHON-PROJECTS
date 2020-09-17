from random import randint
from random import seed

seed(1)

matriz = []

def criando_matriz(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(randint(0, 1000))

    for i in range(len(matriz)):
        print(matriz[i])

def calcula_soma(matriz, linha, coluna, m):
    i_min = max(linha-m, 0)
    i_max = min(linha+m+1, len(matriz))
    soma = 0
    for i in range(i_min, i_max):
        soma += matriz[i][coluna]

    j_min = max(coluna - m, 0)
    j_max = min(coluna + m + 1, len(matriz))
    for j in range(j_min, j_max):
        soma += matriz[linha][j]

    soma -= matriz[linha][coluna]
    return soma


def percorrendo_em_cruz(n, m, matriz):
    maior = -1
    maior_linha = -1
    maior_coluna = -1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = calcula_soma(matriz, i, j, m)
            if soma > maior:
                maior = soma
                maior_linha = i
                maior_coluna = j

    return (maior, maior_linha, maior_coluna)

n = int(input('Insira a dimensão da matriz: '))
m = int(input('Insira o alcance do cálculo da pontuação: '))

criando_matriz(n)
(pontuacao, linha, coluna) = percorrendo_em_cruz(n, m, matriz)


print('-=-'*20)
print('A matriz possui dimensões de {}x{}.'.format(n,n))
print('O range escolhido foi de {}.'.format(m))
print('A maior pontuação foi {} pontos!'.format(pontuacao))
print('-=-'*20)