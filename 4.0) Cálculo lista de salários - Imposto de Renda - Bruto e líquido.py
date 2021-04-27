# Alíquota de Imposto de Renda e montante total anual tributado com funções e sem print/input

sal = [1320.22, 1500.00, 1900.55, 2100.00, 3600.55, 4000.00, 4820.00, 5500.99, 8000.30, 12000.00, 16500.00, 24000.00]

def calculo_ir (sal):
  if sal < 1903.98:
    return sal
  elif sal >= 1903.99  and sal < 2826.65:
    return sal - ((sal * 0.075) - 142.80)
  elif sal >= 2826.65 and sal < 3751.05:
    return sal - ((sal * 0.15) - 354.80)
  elif sal >= 3751.06 and sal < 4664.68:
    return sal - ((sal * 0.225) - 636.13)
  else:
    return sal - ((sal * 0.275) - 869.36)

for salario in sal:  
 salario_liquido = calculo_ir(salario)
 print (f'Salário bruto = R$ {salario} / Salário líquido = R$ {salario_liquido:.2f}')

input ()