import requests
import os

url = "https://jornalfatos.com.br/wp-content/uploads/2020/12/google_.jpg"
r = requests.get(url)

with open("Arquivo baixado.jpg", "wb") as arquivo:
    arquivo.write(r.content)

    if r.status_code == 200:
        print("Download finalizado.")
    else:
        print("URL Inválida!")



