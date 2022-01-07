# Função que calcula movimentos (de 1 a 3 passos) em um
# tabuleiro unidimensional onde é informado o seu tamanho.

# 1) caminho ótimo: quantas roladas para finalizar
# 2) probabilidade do caminho ótimo
# 3) número de combinações possíveis sem dar looping (extrapolar o numero maximo do tabuleiro)

def calculoTabuleiro(casas):
    if casas%3 == 0:
        caminhootimo = casas//3
    else:
        caminhootimo = (casas//3)+1
    
    probabilidade = ((1/3)**caminhootimo)*100
    
    return f"Caminho ótimo: {caminhootimo} tentativas\n\
Probabilidade: {probabilidade:.2f}%\n"

if __name__ == "__main__":
    print(calculoTabuleiro(21))