from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from IPython.display import display


# Passo 1: Escolha o navegador e abra
navegador = webdriver.Chrome()

# Passo 2: Use a função get para entrar no site
navegador.get('https://www.google.com/')

# Passo 3: Escolha o elemento que quer escrever algum dado (campo de busca) e mande o valor da busca
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

# Passo 4: Dê ENTER no elemento (BUSCA)
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


# Passo 5: Procure a informação desejada usando o DEV TOOLS e pegue o dado de um dos elementos (DATA-VALUE)
cotacaodolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

# -- REPETIÇÃO DO PROCEDIMENTO PARA O VALOR DO EURO
navegador.get('https://www.google.com/')
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacaoeuro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

# -- REPETIÇÃO DO PROCEDIMENTO PARA O VALOR DO OURO - mudar endereço para OURO HOJE
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacaoouro = navegador.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute("value")
cotacaoouro = cotacaoouro.replace(",",".")    

# Passo 6: Transforma as cotações em valores reais FLOAT
cotacaodolar = float(cotacaodolar)
cotacaoeuro = float(cotacaoeuro)
cotacaoouro = float(cotacaoouro)

# Fecha o navegador
navegador.quit()

# Passo 7: Abre a tabela com os valores base
tabela = pd.read_excel("Produtos.xlsx")

# Passo 8: Substitui as cotações em cada coluna/linha
tabela.loc[tabela['Moeda']=="Dólar",'Cotação'] = cotacaodolar
tabela.loc[tabela['Moeda']=="Euro",'Cotação'] = cotacaoeuro
tabela.loc[tabela['Moeda']=="Ouro",'Cotação'] = cotacaoouro

# Passo 9: Calcula os novos valores
tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela ['Cotação']
tabela['Preço Final'] = tabela['Preço Base Reais'] * tabela['Margem']

# Passo 10: Demonstra a tabela no terminal e salva uma nova atualizada.
display(tabela)
tabela.to_excel("Tabela atualizada.xlsx", index=False)