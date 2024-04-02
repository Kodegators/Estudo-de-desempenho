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
    return f'{list} sua lista está em ordem, foram necessários {cronometro} segundos'
