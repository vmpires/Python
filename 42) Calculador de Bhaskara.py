listavalores = [10.3,203.0,5.0]
a = listavalores[0]
b = listavalores[1]
c = listavalores[2]

delta = (b**2)-(4*a*c)
divisao = 2*a
if delta < 0 or divisao==0:
    print('Impossivel calcular')
else:
    R1 = (-b+pow(delta,0.5))/(2*a)
    R2 = (-b-pow(delta,0.5))/(2*a)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')