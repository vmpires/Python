# Quick Sort Algorithm

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def QuickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista,inicio,fim)
        QuickSort(lista, inicio, p-1)
        QuickSort(lista, p+1, fim)

if __name__ == "__main__":
    lista = [7,5,1,8,3]
    QuickSort(lista)
    print(lista)
