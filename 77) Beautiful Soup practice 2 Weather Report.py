import requests
from bs4 import BeautifulSoup

search = "Temperatura em Santo André"

url = f"https://www.google.com/search?q={search}"

r = requests.get(url)

s = BeautifulSoup(r.text, "html.parser")

weatherupdate = s.find("div", class_="BNeawe").text


print(weatherupdate)