# Cálculo de descontos com duas listas concatenando
produtos = [50.0, 80.0, 60.0]
descontos = [5.0, 3.0, 10.0]

def aplicacao(produto,desconto):
  final = produto - (produto * desconto/100)
  return final

for i in range (len(produtos)):
  produto = produtos[i]
  desconto = descontos[i]
  final = aplicacao(produto,desconto)
  print (f'O valor original do produto é R$ {produto} e o valor com desconto é de R$ {final}.')
input()