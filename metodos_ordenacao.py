def selectionSort(list):
    n = len(list)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if list[minimo] > list[j]:
                minimo = j
        list[i], list[minimo] = list[minimo], list[i]

