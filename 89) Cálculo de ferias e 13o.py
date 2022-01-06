#Cálculo de avos de férias e 13º salário 

import datetime as dt

def calculaAvos(dataInicio, dataFim, beneficio):
    listadata = dataInicio.split('/')
    dataInicio = dt.date(int(listadata[2]),int(listadata[1]),int(listadata[0]))

    listadata = dataFim.split('/')
    dataFim = dt.date(int(listadata[2]),int(listadata[1]),int(listadata[0]))


    if beneficio == "13":
        intervalo = dataFim - dataInicio
        diasrestantes = intervalo//365
        if diasrestantes.days >= 15:
            return f"{dataFim.month} avos"
        else:
            return f"{dataFim.month-1} avos"
    else:
        if dataFim.day >= 15:
            intervalo = dataFim - dataInicio.replace(year=int(dataFim.year)-1)
            avos = intervalo.days//30
        else:
            intervalo = dataFim - dataInicio.replace(year=int(dataFim.year)-1)
            avos = (intervalo.days//30)-1
        return f"{avos} avos"


if __name__ == "__main__":
    print(calculaAvos("10/10/2010","15/06/2021","ferias"))
    print(calculaAvos("10/10/2010","15/06/2021","13"))
