def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('A média final do aluno é', media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
  if media >= 6:
    print('Aluno Aprovado :)')
  else:
    print('Aluno Reprovado :(')

calcular_media([10, 3, 8, 7])

input()