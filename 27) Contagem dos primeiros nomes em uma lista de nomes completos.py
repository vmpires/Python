from collections import Counter

def Contagem (lista_nomes):
    data = Counter(lista_nomes)
    lista = dict(data)  
    return lista

arquivo = open('Lista_Nomes.txt', 'r')
lista_nomes = arquivo.read()
primeiras_palavras = []
listatratada = []
for line in lista_nomes.split("\n"):
        primeiras_palavras.append(line.split()[0])
for item in primeiras_palavras:
    item.replace("'","")
    listatratada.append(item)
listatratada.sort()
final = Contagem(listatratada)
print(final)
