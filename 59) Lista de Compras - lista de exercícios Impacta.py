inicial = input('Insira os primeiros códigos de produto, se houver: ')
if inicial is None:
    inicial = []
else:
    listastr = inicial.split()
    inicial = []
    for item in listastr:
        inicial.append(int(item))

comando = input('Digite o próximo comando: ')

while comando != "encerrar":

    if comando == "exibir":
        inicial = sorted(inicial)
        for item in range(len(inicial)):
            if item == len(inicial)-1:
                print(inicial[item])
            else:
                print(inicial[item], end=' ')
    
    elif "remover" in comando:
            for word in comando.split():
                if word.isdigit():
                    if int(word) in inicial:
                        inicial.pop(inicial.index(int(word)))
                    else:
                        print(f'código {word} não encontrado')
    else:
        for word in comando.split():
            if word.isdigit():
                inicial.append(int(word))
    comando = input('Digite o próximo comando: ')

if inicial:
    inicial = sorted(inicial)
    for item in range(len(inicial)):
        if item == len(inicial)-1:
            print(inicial[item])
        else:
            print(inicial[item], end=' ')