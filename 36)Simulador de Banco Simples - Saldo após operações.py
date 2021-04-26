listacontas = [["12345", 50], ["12345", -20], ["98765", 25], ["98765", 50]]
dictids = {}

for item in listacontas:
    dictids[item[0]] = 0

for item in listacontas:
    if item[0] in dictids:
        dictids[item[0]] += item[1]

for item, item2 in dictids.items():
    print(f'Conta: {item} / Saldo: {item2}')


