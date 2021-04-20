N = int(50)
aux = 0
aux2 = 0
if N%2==0:
    aux = N-1
    aux2 = N+2
    print(f'{aux} {aux2}')
else:
    aux = N-2
    aux2 = N+1
    print(f'{aux} {aux2}')