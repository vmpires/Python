from forex_python.converter import CurrencyRates

conversor = CurrencyRates()

valor = float(input("Qual o valor em dólar você deseja converter pra real?: "))

valor_convertido = round(conversor.convert("USD", "BRL", valor), 2)

print(f"U$ {valor} = R$ {valor_convertido}")