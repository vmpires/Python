def Notas():
    nota1 = int(input("Insira a Nota 1: "))
    nota2 = int(input("Insira a Nota 2: "))
    return mediafinal(nota1,nota2)
    
def mediafinal(nota1,nota2):
    media = (nota1+nota2)/2
    return media

def VerAprov(media):
    if (media >= 6):
        print (f"Média: {media} - Status: Aprovado")
    else:
        print(f"Média: {media} - Status: Reprovado")
    
VerAprov(Notas())

