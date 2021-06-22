# Cálculo de IMC e dica de dieta

peso = float (input ('Qual o seu peso? '))
altura = float(input ('Qual sua altura? Favor utilizar ponto para separação do número '))
altura = altura **2
imc = peso / altura
imc = int(imc)
print(f'Seu IMC é {imc:.2f}.')
if imc < 16:
  print ('Você está muito abaixo de seu peso ideal!')
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
    print ('Você precisa comer MUITO.')
   elif imc > 16 and imc < 20:
    print ('Você precisa se alimentar mais.')
   elif imc >= 20 and imc < 25:
    print ('Pode comer à vontade!')
   elif imc >= 25 and imc < 30:
    print ('Dá uma segurada amigo.')
   elif imc >= 30 and imc < 40:
    print ('Só salada e treino.')
   elif imc >= 40:
    print ('Fazer cirurgia de redução do estômago')

elif dieta == 'N':
   print ('Adeus.')
else :
   print ('Resposta incorreta.')

input()

 