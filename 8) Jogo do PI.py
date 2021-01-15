numero = input('Olá! Vamos brincar de Pi? Digite um número: ')

numero = int(numero)
fdp = 7

for i in range (numero+1):
  if i % 7 == 0 and i != 0 or i % 10 == 7:
    print ('Pi!')
  else:
    print (i)

input ()  