resinas = input ('Quantas resinas você precisa? ')

resinas = int(resinas)

total = resinas * 8

if total > 60:
  horas = total / 60
  horas = int(horas)
  minutos = total % 60
else:
  horas = 0
  minutos = total

print (f'Faltam {horas} horas e {minutos} minutos para chegar ao seu objetivo.')

input ()