# Bubble Sort Algorithm

def bubble_sort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return(lista)
                
if __name__ == "__main__":
    lista = [7,5,1,8,3]
    print(bubble_sort(lista))
