from bs4 import BeautifulSoup
import requests

# Carrega página do clima #
html = requests.get("http://climatempo.com.br/previsao-do-tempo/cidade/558/santoandre-sp").content

# Caminha sobre o html da página #
soup = BeautifulSoup(html, "html.parser")

# Captura os dados necessários nos elementos html #
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

# Mostra os resultados
print ('Resumo:  ' + resume.text)
print(' Temp. Mínima: ' + tempMin.string)
print(' Temp. Máxima: ' + tempMax.string)