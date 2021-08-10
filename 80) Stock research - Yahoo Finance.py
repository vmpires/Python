import yfinance as yf

# Cria um dicionário com as informações da ação informada / Creates a dict with the stock infos
ticker = yf.Ticker('RAIZ4.SA')

print(f"O valor atualizado da ação é de: R$ {ticker.info['currentPrice']}")