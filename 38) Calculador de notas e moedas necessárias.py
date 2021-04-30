def main():
    valorfloat = float(input('Digite um valor: '))
    cents = valorfloat - int(valorfloat)
    valor = valorfloat - cents
    valor = int(valor)
    print('\nNOTAS:')
    if valor>=100:
        notascem=valor//100
        print(f'{notascem:.0f} nota(s) de R$ 100.00')
    else:
        print('0 nota(s) de R$ 100.00')

    restocem = valor%100
    if restocem>=50:
        notascinquenta=restocem//50
        print(f'{notascinquenta:.0f} nota(s) de R$ 50.00')
    else:
        print('0 nota(s) de R$ 50.00')

    restocinquenta = restocem%50
    if restocinquenta>=20:
        notasvinte = restocinquenta//20
        print(f'{notasvinte:.0f} nota(s) de R$ 20.00')
    else:
        print('0 nota(s) de R$ 20.00')

    restovinte = restocinquenta%20
    if restovinte>=10:
        notasdez = restovinte//10
        print(f'{notasdez:.0f} nota(s) de R$ 10.00')
    else:
        print('0 nota(s) de R$ 10.00')

    restodez = restovinte%10
    if restodez>=5:
        notascinco = restodez//5
        print(f'{notascinco:.0f} nota(s) de R$ 5.00')
    else:
        print('0 nota(s) de R$ 5.00')

    restocinco = restodez%5
    if restocinco>=2:
        notasdois = restocinco//2
        print(f'{notasdois:.0f} nota(s) de R$ 2.00')
    else:
        print('0 nota(s) de R$ 2.00')
    
    print ('MOEDAS:')
    
    print(f'{restocinco%2:.0f} moeda(s) de R$ 1.00')
    
    contador50 = 0
    contador25 = 0
    contador10 = 0
    contador5 = 0

    while cents>=0.50:
        cents = cents - 0.50
        contador50 += 1
    print (f'{contador50} moeda(s) de R$ 0.50')

    while cents>=0.25:
        cents = cents-0.25
        contador25 += 1
    print (f'{contador25} moeda(s) de R$ 0.25')

    while cents>=0.10:
        cents = cents-0.10
        contador10 += 1
    print(f'{contador10} moeda(s) de R$ 0.10')

    while cents>=0.05:
        cents = cents-0.05
        contador5 += 1
    print(f'{contador5} moeda(s) de R$ 0.05')

    if cents>=0.001:
        cents = cents/0.01
    print(f'{cents:.0f} moeda(s) de R$ 0.01\n')
    
    resposta = input('Deseja inserir outro valor?(S/N): ')
    if resposta == 'S' or resposta == 's':
        main()
    else:
        exit()
main()
