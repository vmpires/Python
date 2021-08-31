from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from time import sleep

# Carregamento de informações de login e senha em arquivo externo
f = open("config.json", 'r')
key = json.load(f)


# Definição do Browser e entrada no Linkedin
browser = webdriver.Chrome()
browser.get("https://www.linkedin.com/login")

# Login Automatizado
input_email = browser.find_element_by_id("username")
input_email.send_keys(key["user"])

input_senha = browser.find_element_by_id("password")
input_senha.send_keys(key["pass"])

btn_login = browser.find_element_by_xpath("//button[@type='submit']")
btn_login.click()

# Busca Personalizada
busca = browser.find_element_by_xpath("//input[@placeholder='Pesquisar']")
busca.send_keys("Python")
busca.send_keys(Keys.RETURN)

sleep(3.0)

vagas = browser.find_element_by_xpath("//button[@aria-label='Vagas']")
vagas.click()

input()