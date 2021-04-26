listacontas = [["12345", 50], ["12345", -20], ["98765", 25], ["98765", 50]]
saldos = {}

for conta in listacontas:
    saldos[conta[0]] = 0

for conta in listacontas:
    if conta[0] in saldos:
        saldos[conta[0]] += conta[1]

for conta, saldo in saldos.items():
    print(f'Conta: {conta} / Saldo: {saldo}')


