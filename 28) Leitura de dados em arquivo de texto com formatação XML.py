import xmltodict

f = open ('filmes.txt', 'r')
x = f.read()
doc = xmltodict.parse(str(x))

print(f"O nome do filme é {doc['filmes']['filme']['titulo']}")
print(f"O resumo do filme é {doc['filmes']['filme']['resumo']}")
print(f"O filme tem como ator: {doc['filmes']['filme']['elenco']['ator'][0]}")