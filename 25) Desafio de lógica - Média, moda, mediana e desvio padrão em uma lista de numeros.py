import statistics
import math
from collections import Counter
def Media (lista_numeros):
    soma = 0
    for item in lista_numeros:      
        soma += item
    media = (soma/len(lista_numeros))
    return media
def Moda (lista_numeros):
    data = Counter(lista_numeros)
    moda = dict(data)
    modafinal = [keys for keys, values in moda.items() if values == max(list(data.values()))]
    return modafinal[0]
def Mediana (lista_numeros):
    mediana = 0
    lista_numeros.sort()
    if len(lista_numeros) % 2 == 0:
        primeira_mediana = lista_numeros[len(lista_numeros) // 2]
        segunda_mediana = lista_numeros[len(lista_numeros) // 2 - 1]
        mediana = (primeira_mediana + segunda_mediana) / 2
    else:
        mediana = lista_numeros[len(lista_numeros) // 2]
    return mediana
def DesvioPad (lista_numeros):
    somadif = 0
    desviopadrao = 0
    media = Media(lista_numeros)
    for item in lista_numeros:  
        somadif += (item-media)**2    
    desviopadrao = somadif/len(lista_numeros)
    return math.sqrt(desviopadrao)

lista_numeros = [10000,30000,90000,30000]
print (f'Média: {Media(lista_numeros)}')
print (f'Moda: {Moda(lista_numeros)}')
print (f'Mediana: {Mediana(lista_numeros)}')
print (f'Desvio Padrão: {DesvioPad(lista_numeros)}')