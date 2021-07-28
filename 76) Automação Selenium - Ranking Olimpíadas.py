from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Passo 1: Escolha o navegador e abra
option = webdriver.ChromeOptions()
option.add_argument('headless') #Set the parameters of the option
navegador = webdriver.Chrome(chrome_options=option) # Open Google Chrome

# Passo 2: Use a função get para entrar no site
navegador.get('https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm')

# Passo 5: Procure a informação desejada usando o DEV TOOLS e pegue o dado de um dos elementos (DATA-VALUE)
primeirolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[2]/div/a').text

primeiroouros = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[3]/a').text

primeiropratas = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[4]/a').text

primeirobronzes = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[5]/a').text

segundolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[2]/div/a').text

segundoouros = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[3]/a').text

segundopratas = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[4]/a').text

segundobronzes = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[5]/a').text

terceirolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[2]/div/a').text

terceiroouros = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[3]/a').text

terceiropratas = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[4]/a').text

terceirobronzes = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[5]/a').text

# Fecha o navegador
navegador.quit()

print(f'1º - {primeirolugar}: Ouro: {primeiroouros} | Prata: {primeiropratas}| Bronze: {primeirobronzes}\n')
print(f'2º - {segundolugar}: Ouro: {segundoouros} | Prata: {segundopratas}| Bronze: {segundobronzes}\n')
print(f'3º - {terceirolugar}: Ouro: {terceiroouros} | Prata: {terceiropratas}| Bronze: {terceirobronzes}\n')
