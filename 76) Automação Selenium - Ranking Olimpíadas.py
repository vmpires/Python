from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('headless') 
navegador = webdriver.Chrome(chrome_options=option)


navegador.get('https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm')

primeirolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[2]/div/a').text

primeiroouros = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[3]/a').text)

primeiropratas = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[4]/a').text)

primeirobronzes = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[1]/td[5]/a').text)

segundolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[2]/div/a').text

segundoouros = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[3]/a').text)

segundopratas = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[4]/a').text)

segundobronzes = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[2]/td[5]/a').text)

terceirolugar = navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[2]/div/a').text

terceiroouros = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[3]/a').text)

terceiropratas = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[4]/a').text)

terceirobronzes = int(navegador.find_element_by_xpath(
    '//*[@id="medal-standing-table"]/tbody/tr[3]/td[5]/a').text)

# Fecha o navegador
navegador.quit()
print("\nTop 3 Countries - 2020 Olympics - Japan\n")
print(f'1º - {primeirolugar}: Gold: {primeiroouros} | Silver: {primeiropratas} | Bronze: {primeirobronzes} | Total: {primeiroouros+primeiropratas+primeirobronzes}\n')
print(f'2º - {segundolugar}: Gold: {segundoouros} | Silver: {segundopratas} | Bronze: {segundobronzes} | Total: {segundoouros+segundopratas+segundobronzes}\n')
print(f'3º - {terceirolugar}: Gold: {terceiroouros} | Silver: {terceiropratas} | Bronze: {terceirobronzes} | Total: {terceiroouros+terceiropratas+terceirobronzes}\n')
