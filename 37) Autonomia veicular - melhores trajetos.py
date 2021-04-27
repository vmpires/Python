eficiencia = 15
tanque = 40
autonomia = tanque*eficiencia
trajetosdict = {}
trajetos = [["Trajeto 1", 120], ["Trajeto 2", 150], ["Trajeto 3", 180], ["Trajeto 4", 200]]

for trajeto in trajetos:
    trajetosdict[trajeto[0]]=trajeto[1]

print(f'Autonomia do veículo: {autonomia:.0f}km')
listanomestrajetos = list(trajetosdict.keys())
listakmtrajetos = list(trajetosdict.values())
listanova = list(zip(listakmtrajetos,listanomestrajetos))
listanova = sorted(listanova)

for trajeto in listanova:
    if autonomia-trajeto[0] >= 0:
        autonomia = autonomia-trajeto[0]
        if trajeto in listanova:
            print(f'{trajeto[1]} realizado.')

if autonomia != 0:
    print(f'Restaram {autonomia} kilometros de autonomia.')
else:
    print(f'Uau, você usou toda gasolina!')
