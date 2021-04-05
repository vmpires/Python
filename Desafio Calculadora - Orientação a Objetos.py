class Calc (object):
    primeiro_valor = None
    segundo_valor = None

    def Soma(primeiro_valor, segundo_valor):
        soma = (primeiro_valor + segundo_valor)
        print (f'Soma = {soma}')

    def Subt(primeiro_valor, segundo_valor):
        soma = (primeiro_valor - segundo_valor)
        print (f'Subtração = {soma}')

    def Mult(primeiro_valor, segundo_valor):
        soma = (primeiro_valor * segundo_valor)
        print (f'Multiplicação = {soma}')

    def Div(primeiro_valor, segundo_valor):
        soma = (primeiro_valor / segundo_valor)
        print (f'Divisão = {soma}')

primeiro_valor = float(input('Qual o primeiro valor? '))
segundo_valor = float(input('Qual o segundo valor? '))

Calc.Soma(primeiro_valor,segundo_valor)
Calc.Subt(primeiro_valor,segundo_valor)
Calc.Mult(primeiro_valor,segundo_valor)
Calc.Div(primeiro_valor,segundo_valor)