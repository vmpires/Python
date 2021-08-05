def Potencia(numero):
    return numero ** 2


if __name__ == "__main__":
    lista = [2,4,6,8]
    resultados = list(map(Potencia, lista))
    
    print(resultados)