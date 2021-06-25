import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 2

# Passo 1 - Entrar no Google Drive
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.click(733,40, clicks=2)
link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

# Passo 2 - Entrar na pasta EXPORTAR
time.sleep(3)
pyautogui.click(402,299, clicks=2)
time.sleep(3)

# Passo 3 - Baixar e extrair informações do arquivo
pyautogui.click(389,385) # Clicar no arquivo
pyautogui.click(1217,191) # Clicar na reticências (alterar posições)
pyautogui.click(1035,527) # Clicar no Download (alterar posições)
time.sleep(5)

tabela = pd.read_excel(r"C:\Users\50s\Downloads\Vendas - Dez.xlsx")
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Passo 5 - Enviar o Faturamento e a Quantidade por e-mail
pyautogui.hotkey('ctrl','t')
link = 'https://mail.google.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(57,208)
email = 'vctprs@gmail.com'
pyperclip.copy(email)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyautogui.press('tab')
subject = "Atualização diária de Faturamento e Quantidade"
pyperclip.copy(subject)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
body = f"""Olá, boa noite!

Faturamento = R$ {faturamento:,.2f}

Quantidade total = {quantidade:,}

Att.

Victor Milhome Pires
"""
pyperclip.copy(body)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')