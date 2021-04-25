listatotal = [['Gabigol', 10, 15, 20, 10, 22],['Zico', 10, 30, 20, 20, 26],['Adriano', 10, 15, 20, 10, 10],['Junior', 10, 5, 10, 14, 6]]
listagols = []
listajogadores = []
media = 0
listamedias = []
dictgols = {}

for item in listatotal:
    listagols.append(item[1:])

for item in listatotal:
    listajogadores.append(item[0])

for gols in listagols:
    media = sum(gols)/len(gols)
    listamedias.append(media)

for item in listajogadores:
    dictgols[item] = 0
    for i in range (len(dictgols)):
        dictgols[item] = listamedias[i]

x = list(dictgols.values())
y = list(dictgols.keys())
almostlist = []
for i in range(len(x)):
    almostlist.append([x[i],y[i]])
almostlist = sorted(almostlist, reverse=True)
# Há a forma fácil e a forma difícil de montar a lista de jogadores + media, vou usar a forma difícil neste programa (acima).
# Forma fácil abaixo: 
#almostlist = list(zip(x,y))


# Há a forma fácil e a forma difícil de ordenar a lista, vou usar a forma difícil neste programa (acima).
# Forma fácil abaixo: 
# listaordenada = sorted(dictgols.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
	print(almostlist[i])
