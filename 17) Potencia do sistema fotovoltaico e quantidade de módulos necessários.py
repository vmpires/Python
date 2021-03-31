import math

def CalcularSistema(consumo):
    potenciamodulo = 330
    horasol = 4.6
    eficiencia = 0.85
    precomodulo = 1000
    maodeobra = 2500
    precoinversor = 3000
    precostring = 500
    precohomolog = 500
    conta = consumo*0.7
    potencia = consumo / (30 * horasol * eficiencia)
    modulos = (potencia * 1000) / potenciamodulo
    modarredondado = math.ceil(modulos)
    geracao = (modarredondado * potenciamodulo * horasol * 30 * eficiencia) / 1000
    valorsistema = (modarredondado*precomodulo)+maodeobra+precoinversor+precostring+precohomolog
    print (f'A potência do sistema é de {potencia:.2f} kWp e são necessários aproximadamente {modarredondado:.0f} \nmódulos fotovoltaicos para sua implementação.\nA geração mensal de energia é de aproximadamente {geracao:.2f} kilowatts.\nO valor da implementação do serviço é de R$ {valorsistema:.2f}.')
    CalcularPayback(valorsistema,conta)


def CalcularPayback(valorsistema,conta):   
    mesestotais = valorsistema/conta
    mesesarredondados = math.ceil(mesestotais)
    if mesesarredondados >= 12:
        anos = (mesesarredondados//12)
        mesesrestantes = mesesarredondados%12
        if mesesrestantes == 0:
            print(f'Seu sistema tem um payback de aproximadamente {anos} anos.')
        else:
            print(f'Seu sistema tem um payback de aproximadamente {anos:.0f} anos e {mesesrestantes} meses.')
    else:
        print (f'Seu sistema tem payback de aproximadamente {mesestotais} meses.')    

consumo = int(input('Qual o seu consumo médio anual em kilowatts? '))
CalcularSistema(consumo)

input ()