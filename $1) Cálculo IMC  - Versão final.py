# Cálculo de IMC e dica de dieta

peso = float (input ('Qual o seu peso? '))
altura = float(input ('Qual sua altura? Favor utilizar ponto para separação do número '))
altura = altura **2
imc = peso / altura
imc = int(imc)
print(f'Seu IMC é {imc:.2f}.')
if imc < 16:
  print ('Bitch, you dead')
elif imc >= 16 and imc < 20:
 print ('Você está com subpeso.')
elif imc >= 20 and imc < 25:
 print ('Você está normal.')
elif imc >= 25 and imc < 30:
 print ('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
 print ('Você está obeso.')
elif imc >= 40:
 print ('Você está com obesidade mórbida.')

dieta = input('Gostaria de uma dica de dieta? Responda S para Sim e N para Não ')
 
if dieta == 'S':
   if imc < 16:
    print ('Você já tá morto fera.')
   elif imc > 16 and imc < 20:
    print ('Come uns bacon aí caralho!')
   elif imc >= 20 and imc < 25:
    print ('Pode comer qlqr porra!')
   elif imc >= 25 and imc < 30:
    print ('Dá uma segurada lek...')
   elif imc >= 30 and imc < 40:
    print ('Tá fudido, vai ter que comer só salada e treinar...')
   elif imc >= 40:
    print ('Faz uma cirurgia no estômago aí na moral.')

elif dieta == 'N':
   print ('Vai se fuder então!')
else :
   print ('Sabe nem responder hein fera?!')

input()

 