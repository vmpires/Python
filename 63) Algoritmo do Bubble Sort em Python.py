def bubble_sort(lista):
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return(lista)
                

if __name__ == "__main__":

    lista = []
    resposta = 's'
    while resposta == 's':
        numero = input("Digite um número: ")
        lista.append(int(numero))
        resposta = input('Deseja digitar outro?(s/n): ')

    print(bubble_sort(lista))
