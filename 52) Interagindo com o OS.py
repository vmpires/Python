import os
import platform
import shutil
from distutils.dir_util import copy_tree

# 2 formas possíveis para descobrir o nome do OS
print(os.name)
print(platform.system())

# Informações sobre o ambiente do sistema
for item in os.environ.items():
    print(item)

# ID do processo atual
print(os.getpid())

# Caminho atual de um arquivo
print(os.getcwd())

# Pasta do arquivo
print(f'Pasta do arquivo: {os.path.dirname(__file__)}')

# Imprimir caminho e nome do arquivo de outra forma
print(f'Nome do arquivo INTEIRO com caminho: {__file__}')
print(f'Nome do arquivo: {os.path.basename(__file__)}')

# Caminho absoluto do arquivo
print(f'Caminho absoluto: {os.path.abspath(__file__)}')

# Mostrando caminho da pasta
print(os.listdir())  #Dentro do parenteses pode ser indicada qualquer caminho do sistema (usando \\)




