import pyshorteners

# Recebe a URL original
urloriginal = input ('Digite uma URL válida: ')

# Carrega a biblioteca
s = pyshorteners.Shortener()

# Gera URL encurtada
shorUrl = s.tinyurl.short(urloriginal)

# Mostra URL encurtada
print (f"URL encurtada: {shorUrl}")