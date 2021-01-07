# Alíquota e valor devido do imposto de renda

print ('Olá! Meu nome é Monty Python e este programa irá colher o valor do seu salário ')
print ('e descobrir qual a alíquota, bem como valor do seu Imposto de Renda a ser recolhido mensalmente na fonte.')
salario = float(input('Qual o valor do seu salário? Utilize ponto final para separar os centavos caso necessário. '))

if salario < 1903.98:
  print ('Fique tranquilo, este valor não é tributado.')
elif salario >= 1903.99  and salario < 2826.65:
  mensal = (salario * 0.075) - 142.80
  total = mensal *12
  print (f'A alíquota devida é de 7,5% ao mês, totalizando um desconto mensal de R$ {mensal:.2f}. O montante total anual a ser tributado é de R$ {total}')  
elif salario >= 2826.65 and salario < 3751.05:  
  mensal = (salario * 0.15) - 354.80
  total = mensal *12
  print (f'A alíquota devida é de 15% ao mês, totalizando um desconto mensal de R$ {mensal:.2f}. O montante total anual a ser tributado é de R$ {total}')
elif salario >= 3751.06 and salario < 4664.68:
  mensal = (salario * 0.225) - 636.13
  total = mensal *12
  print (f'A alíquota devida é de 22,5% ao mês, totalizando um desconto mensal de R$ {mensal:.2f}. O montante total anual a ser tributado é de R$ {total}')
else:
  mensal = (salario * 0.275) - 869.36
  total = mensal *12
  print (f'A alíquota devida é de 27,5% ao mês, totalizando um desconto mensal de R$ {mensal:.2f}. O montante total anual a ser tributado é de R$ {total}') 

input ()  