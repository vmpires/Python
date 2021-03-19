import os
import time

arquivo = input('Insira o caminho do arquivo desejado: ')

print('O nome do arquivo é', arquivo)
print('Foi modificado pela última vez em', time.ctime(os.path.getmtime(arquivo)))
print('E seu tamanho é de', os.path.getsize(arquivo), 'bytes.')