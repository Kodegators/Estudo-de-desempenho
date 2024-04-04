import time

def selectionSort(list):
    n = len(list)
    inicio = time.time()
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if list[minimo] > list[j]:
                minimo = j
        list[i], list[minimo] = list[minimo], list[i]
    fim = time.time()
    cronometro = fim-inicio
    return f'{list}\nsua lista está em ordem, foram necessários {cronometro:.2f} segundos'


def insertionSort(list):
    n = len(list)
    inicio = time.time()
    for i in range(1, n):
        key = list[i]
        x = i - 1
        while x >= 0 and list[x] > key:
            list[x + 1] = list[x]
            x = x - 1
        list[x + 1] = key
    fim = time.time()
    cronometro = fim-inicio
    return f'{list}\nSua lista está em ordem, foram necessários {cronometro:.2f} segundos'
