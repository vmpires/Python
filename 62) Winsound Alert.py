import winsound

frequency = 37
duration = 7000

resposta = input('Bem vindo! Responda S para ouvir música eletrônica no Windows (coloque os fones!): ')

if resposta == "s" or resposta == "S":
    winsound.Beep(frequency, duration)
else:
    resposta = input("Ok que tal então um som clássico do Windows? Te darei outra chance de apertar S: ")
    if resposta == "s" or resposta == "S":
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    else:
        print('Então Adeus.')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

