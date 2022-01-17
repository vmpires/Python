# Selection Sort Algorithm - largest complexity among sort algorithms

def SelectionSort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            lista[j],lista[min_index] = lista[min_index], lista[j]
    return lista


if __name__ == "__main__":

    lista = [7,5,1,8,3]
    print(SelectionSort(lista))
