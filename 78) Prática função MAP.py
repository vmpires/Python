def Potencia(numero):
    return numero ** 2

def Imposto(numero):
    return numero *1.1


if __name__ == "__main__":
    lista = [2,4,6,8]
    potencia = list(map(Potencia, lista))
    imposto = list(map(Imposto, lista))
    
    print(potencia)
    print(imposto)