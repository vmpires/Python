from random import randrange


def main(randomnum,contador):
    digitado = int(input('Adivinhe o número gerado entre 0 e 100: '))
    if digitado == randomnum:
        contador += 1
        print(f'Parabéns! Você acertou, o número é {randomnum} e precisou de {contador} tentativas.')    
    elif digitado > randomnum:
        print('O número digitado é maior que o correto.')
        contador += 1
        main(randomnum,contador)
    else:
        print('O número digitado é menor que o correto.')
        contador += 1
        main(randomnum,contador)

contador = 0
randomnum = randrange(0,101)
main(randomnum,contador)