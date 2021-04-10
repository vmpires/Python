from collections import Counter

def Contagem (lista_nomes):
    data = Counter(lista_nomes)
    return data

arquivo = open('Lista_Nomes.txt', 'r')
lista_nomes = arquivo.read()
splitted1 = lista_nomes.replace("\n"," ")
splitted2 = splitted1.replace(" ",",")
splitted3 = splitted2.split(',')
splitted3.sort()

final = Contagem(splitted3)
print(final)