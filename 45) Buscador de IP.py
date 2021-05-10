import socket as s

# Host desejado
host = 'github.com'

# Captura o IP do host informado
ip = s.gethostbyname(host)

# Exibe o resultado
print (f'O IP do {host} é: {ip}.')