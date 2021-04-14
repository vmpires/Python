lista = [[10,10],[8,4],[9,6]]
soma = 0
contador = 0
contador2 = 0
for item in lista:
    for i in item:
        soma += i
        contador += 1
media = soma/contador
for item in lista:
    for i in item:
        if i>media:
            contador2+=1
print(f'Há {contador2} números acima da média da matriz.')








