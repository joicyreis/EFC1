'''
CPA - Algoritmos de Ordenação

__author__ = "Joicy Paula dos Reis"
Matrícula 201920347
'''

import numpy as np # para funções e estruturas de arrays
import time # Para o tempo de execução
import matplotlib.pyplot as plt # para plotagem dos gráficos
import random


def analisa(algoritmo, array, complemento=None):
    ini= time.time()
    comparacoes=algoritmo(array, complemento)
    fim = time.time()
    return (comparacoes, fim-ini)


def swap (array, a, b):
    aux = array[a]
    array[a] = array[b]
    array[b] = aux


def geraArrayAleatorio(n, valor_min=0, valor_max=100):
    return np.random.randint(valor_min, valor_max, (n))


def geraArrayOrdenado(inicio, fim, passo=1):
    return np.arange(inicio, fim, passo)





def insertionSort(array, complemento=None):
    comparacoes = 0
    # O insertion inicia no segundo elemento, pois irá fazer comparações a esquerda.
    # Então para iterador i indo de 1 até tamanho do array - 1 (função range):
    for i in range(1, len(array)):
        # key recebe o valor que está na posição i do array
        # Iterador j recebe o valor na posição anterior (i-1)
        key = array[i]
        j = i - 1

        # Enquanto j for maior ou igual a 0 e o valor chave for menor que o valor
        # na posição j do array: 
        while j >= 0 and key < array[j]:
            comparacoes += 1 # incrementa o número de comparações.
            array[j+1] = array[j] # replica o valor presente na posição anterior para a posterior
            j = j - 1 # decrementa o valor de j
        comparacoes += 1 # a saida do while conta como comparação

        # Salva a chave na última posição encontrada de troca.
        array[j+1] = key
    return comparacoes




def mergeSort(array,complemento=None):
    comparacoes = 1 # o if para saber se o array é um único valor conta como uma comparação
    if (len(array) > 1):
        
        meio = len(array) // 2 # posição de divisão
        esquerda = array[:meio].copy() # copy é usado pra copiar os valores para um novo array
        direita  = array[meio:].copy() # porque o NumPy retorna uma visão que altera os valores do original.

        # Ordena os lados
        comparacoes += mergeSort(esquerda)
        comparacoes += mergeSort(direita)


        # Merge
        # Compara os vetores ordenados esquerda e direita
        # voltando a formar o array original, ordenado.    
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1
            comparacoes += 1

        # Quando os valores dentro de um dos vetores filhos
        # acabar, então deve-se realocar os valores restantes
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1
            comparacoes += 1
        
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1
            comparacoes += 1

        return comparacoes + 3 # cada while executa uma vez a mais pra sair do loop
    else: 
        return comparacoes




def selectionSort(array, complemento=None):
    comparacoes = 0
    for i in range(len(array)):
        min_id = i # Considera que i é o valor mínimo

        # Percorre o vetor, a partir de i, em busca de um novo mínimo (se houver)
        for j in range(i+1, len(array)):
            comparacoes += 1
        if (array[j] < array[min_id]):
            min_id = j
        
        # Troca o valor em i com o valor em min_id
        swap(array, i, min_id)
    return comparacoes




def bubbleSort(array, complemento=None):
    comparacoes=0
    for i in range (len(array)):
        for j in range (len(array)-1):
            comparacoes+=1
            if (array[j] > array[j+1]):
                swap(array, j, j+1)
    return comparacoes




def heapify(array, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    comparacoes = 3 # 3 ifs, 3 comparações
    if (esquerda < n and array[i] < array[esquerda]): 
            maior = esquerda
    if (direita < n and array[maior] < array[direita]): 
            maior = direita
    if maior != i:
            swap(array, i, maior)
            comparacoes += heapify(array, n, maior)

    return comparacoes

def heapSort(array, complemento=None):
    n = len(array)
    comparacoes = 0
    for i in range(n//2, -1, -1):
            comparacoes += heapify(array, n, i)

    for i in range(n-1, 0, -1):
            swap(array, i, 0)
            comparacoes += heapify(array, i, 0)
        
    return comparacoes



def quickSort(array, complemento):
    ini = complemento[0]
    fim = complemento[1]
    comparacoes = 1 # Primeiro if
    if (ini < fim):
        pivo = array[fim]
        
        i = ini - 1
        for j in range(ini, fim):
            comparacoes += 1
            if array[j] <= pivo:
                i += 1
                swap(array, i, j)
        
        swap(array, i+1, fim)

        comparacoes += quickSort(array, (ini, i))
        comparacoes += quickSort(array, (i+2, fim))
        
    return comparacoes


def quickSortAleatorizado(array, complemento):
    ini = complemento[0]
    fim = complemento[1]
    comparacoes = 1 # Primeiro if
    if (ini < fim):
        pivo = array[random.randrange(ini, fim)] # pivo aleatorio
        
        i = ini - 1
        for j in range(ini, fim):
            comparacoes += 1
            if array[j] <= pivo:
                i += 1
                swap(array, i, j)
        
        swap(array, i+1, fim)

        comparacoes += quickSort(array, (ini, i))
        comparacoes += quickSort(array, (i+2, fim))
        
    return comparacoes

if __name__ == '__main__':
    # Amostras
    arrayCrescente   = geraArrayOrdenado(0, 1000, 5)
    arrayDecrescente = geraArrayOrdenado(1000, 0, -5)
    arrayAleatorio   = geraArrayAleatorio(len(arrayCrescente), 0, 1000)

    # Casos: [melhor caso, pior caso, caso médio]
    algoritmos = [
        [
            analisa(insertionSort, arrayCrescente.copy(), None), 
            analisa(insertionSort, arrayDecrescente.copy(), None), 
            analisa(insertionSort, arrayAleatorio.copy(), None)
        ],
        [
            analisa(mergeSort, arrayCrescente.copy(), None), 
            analisa(mergeSort, arrayDecrescente.copy(), None), 
            analisa(mergeSort, arrayAleatorio.copy(), None)
        ],
        [
            analisa(selectionSort, arrayCrescente.copy(), None), 
            analisa(selectionSort, arrayDecrescente.copy(), None), 
            analisa(selectionSort, arrayAleatorio.copy(), None)
        ],
        [
            analisa(bubbleSort, arrayCrescente.copy(), None), 
            analisa(bubbleSort, arrayDecrescente.copy(), None), 
            analisa(bubbleSort, arrayAleatorio.copy(), None)
        ],
        [
            analisa(heapSort, arrayDecrescente.copy(), None), 
            analisa(heapSort, arrayCrescente.copy(), None), 
            analisa(heapSort, arrayAleatorio.copy(), None)
        ],
        [
            analisa(quickSort, arrayAleatorio.copy(), (0, len(arrayCrescente)-1)), 
            analisa(quickSort, arrayDecrescente.copy(), (0, len(arrayCrescente)-1)), 
            analisa(quickSort, arrayAleatorio.copy(), (0, len(arrayCrescente)-1))
        ],
    ]

    # Largura e posição das barras
    larguraBarra = 0.14
    pos1 = np.arange(3)
    pos2 = [x + larguraBarra for x in pos1]
    pos3 = [x + larguraBarra for x in pos2]
    pos4 = [x + larguraBarra for x in pos3]
    pos5 = [x + larguraBarra for x in pos4]
    pos6 = [x + larguraBarra for x in pos5]

    #Plotando numero de comparções por algoritmo
    plt.figure(figsize=(15,5))
    plt.bar(pos1, [algoritmos[0][j][0] for j in range(3)], color='#2596be', width=larguraBarra, label='Insertion Sort')
    plt.bar(pos2, [algoritmos[1][j][0] for j in range(3)], color='#e28743', width=larguraBarra, label='Merge Sort')
    plt.bar(pos3, [algoritmos[2][j][0] for j in range(3)], color='#eab676', width=larguraBarra, label='Select Sort')
    plt.bar(pos4, [algoritmos[3][j][0] for j in range(3)], color='#063970', width=larguraBarra, label='Bubble Sort')
    plt.bar(pos5, [algoritmos[4][j][0] for j in range(3)], color='#76b5c5', width=larguraBarra, label='Heap Sort')
    plt.bar(pos6, [algoritmos[5][j][0] for j in range(3)], color='#873e23', width=larguraBarra, label='Quick Sort')


    plt.xticks([r + larguraBarra*2.5 for r in range(3)], ["Melhor Caso", "Pior Caso", "Aleatório"])
    plt.ylabel('Número de Comparações')
    plt.title(f'Número de Comparações de Cada Algoritmo para o Melhor Caso, Pior Caso e Entrada Aleatória (n={len(arrayCrescente)})')
    plt.grid(axis='y', linewidth=0.5, color='#cccccc', linestyle=':')
    plt.legend()
    plt.show()

    #Plotando tempo de execução por algoritmo
    plt.close()
    plt.figure(figsize=(15,5))
    plt.bar(pos1, [algoritmos[0][j][1]*0.001 for j in range(3)], color='#2596be', width=larguraBarra, label='Insertion Sort')
    plt.bar(pos2, [algoritmos[1][j][1]*0.001 for j in range(3)], color='#e28743', width=larguraBarra, label='Merge Sort')
    plt.bar(pos3, [algoritmos[2][j][1]*0.001 for j in range(3)], color='#eab676', width=larguraBarra, label='Select Sort')
    plt.bar(pos4, [algoritmos[3][j][1]*0.001 for j in range(3)], color='#063970', width=larguraBarra, label='Bubble Sort')
    plt.bar(pos5, [algoritmos[4][j][1]*0.001 for j in range(3)], color='#873e23', width=larguraBarra, label='Heap Sort')
    plt.bar(pos6, [algoritmos[5][j][1]*0.001 for j in range(3)], color='#76b5c5', width=larguraBarra, label='Quick Sort')


    plt.xticks([r + larguraBarra*2.5 for r in range(3)], ["Melhor Caso", "Pior Caso", "Aleatório"])
    plt.ylabel('Tempo de Execução (ms)')
    plt.title(f'Tempo de Execução de Cada Algoritmo para o Melhor Caso, Pior Caso e Entrada Aleatória (n={len(arrayCrescente)})')
    plt.grid(axis='y', linewidth=0.5, color='#cccccc', linestyle=':')
    plt.legend()
    plt.show()

    quickotimizado = [
        analisa(quickSortAleatorizado, arrayAleatorio.copy(), (0, len(arrayCrescente)-1)), 
        analisa(quickSortAleatorizado, arrayDecrescente.copy(), (0, len(arrayCrescente)-1)), 
        analisa(quickSortAleatorizado, arrayAleatorio.copy(), (0, len(arrayCrescente)-1))
    ]

    #Plotando número de comparações por quick sort
    plt.close()
    plt.figure(figsize=(15,5))
    plt.bar(pos1, [algoritmos[5][j][0] for j in range(3)], color='#2596be', width=larguraBarra, label='Tradicional')
    plt.bar(pos2, [quickotimizado[j][0] for j in range(3)], color='#e28743', width=larguraBarra, label='Otimizado')


    plt.xticks([r + larguraBarra*0.5 for r in range(3)], ["Melhor Caso", "Pior Caso", "Aleatório"])
    plt.ylabel('Número de Comparações')
    plt.title(f'Número de Comparações de Cada Quick para o Melhor Caso, Pior Caso e Entrada Aleatória (n={len(arrayCrescente)})')
    plt.grid(axis='y', linewidth=0.5, color='#cccccc', linestyle=':')
    plt.legend()
    plt.show()

    #Plotando tempo de execução por quick sort
    plt.figure(figsize=(15,5))
    plt.bar(pos1, [algoritmos[5][j][1]*0.001 for j in range(3)], color='#2596be', width=larguraBarra, label='Tradicional')
    plt.bar(pos2, [quickotimizado[j][1]*0.001 for j in range(3)], color='#e28743', width=larguraBarra, label='Otimizado')


    plt.xticks([r + larguraBarra*0.5 for r in range(3)], ["Melhor Caso", "Pior Caso", "Aleatório"])
    plt.ylabel('Tempo de Execução (ms)')
    plt.title(f'Tempo de Execução de Cada Quick para o Melhor Caso, Pior Caso e Entrada Aleatória (n={len(arrayCrescente)})')
    plt.grid(axis='y', linewidth=0.5, color='#cccccc', linestyle=':')
    plt.legend()
    plt.show()

    print(algoritmos[5])
    print("###")
    print(quickotimizado)