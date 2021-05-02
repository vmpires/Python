from random import randrange

def RequererOpcoes():
    opcoes = 0
    while opcoes != 'finalizado':
        opcoes = input("Digite um nome a ser sorteado, ao acabar, digite 'finalizado': ")
        listaopcoes.append(opcoes)
def Sortear():
    alcance = len(listaopcoes)-1
    sorteado = randrange(0,alcance)
    print(f'Nome sorteado: {listaopcoes[sorteado]}.')

listaopcoes = []
RequererOpcoes()
Sortear()