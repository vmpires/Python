import os
import platform
import shutil
from distutils.dir_util import copy_tree

#Criando pastas
os.mkdir('C:\\Users\\50s\\Desktop\\mkdirtest') # Pode ser usado como caminho relativo ou absoluto
# Não funciona com recursividade (subdiretórios)

# Para criar mais pastas, usar o recurso abaixo (funciona recursivamente)
os.makedirs('C:\\Users\\50s\\Desktop\\mkdirtest2\\dir2\\dir3\\dir4')

# Movendo e renomeando arquivos com OS.RENAME
os.rename('C:\\Users\\50s\\Desktop\\teste.py','C:\\Users\\50s\\Desktop\\testerename.py')
# Serve para arquivos e pastas

# Movendo arquivos de pastas
os.rename('C:\\Users\\50s\\Desktop\\Nova Pasta\\Novo Documento de Texto.txt','C:\\Users\\50s\\Desktop\\Nova Pasta (2)\\Novo Documento de Texto.txt')

# Copiando arquivos
#shutil.copy2('C:\\Users\\50s\\Desktop\\testerename.py','C:\\Users\\50s\\Desktop\\testerename2.py')

# Copiando pastas inteiras com seus arquivos usando o pacote distutils.dir_util e a função copy_tree
copy_tree('C:\\Users\\50s\\Desktop\\Nova Pasta', 'C:\\Users\\50s\\Desktop\\Nova Pasta (2)')

# Removendo arquivos com os.remove OBS: Não funciona com PASTAS
os.remove('C:\\Users\\50s\\Desktop\\testerename2.py')

# Removendo pastas VAZIAS
os.removedirs('C:\\Users\\50s\\Desktop\\Nova Pasta')

# Removendo pastas COM ARQUIVOS
shutil.rmtree('C:\\Users\\50s\\Desktop\\Nova Pasta')

# Checando a existência de pastas (APENAS) antes de sua criação
if (not os.path.isdir('C:\\Users\\50s\\Desktop\\Nova Pasta')):
   os.mkdir('C:\\Users\\50s\\Desktop\\Nova Pasta')

# Checando a existência de arquivo (APENAS)
if os.path.isfile('C:\\Users\\50s\\Desktop\\testerename.py'):
    print("Arquivo existe")
else:
    print("Arquivo não existe")

# Para apenas saber a existencia, usar:
print(os.path.exists('C:\\Users\\50s\\Desktop\\testerename.py'))

# Criando arquivos
open('C:\\Users\\50s\\Desktop\\criandoarquivo.txt', 'w+') # WRITE - deleta o conteúdo, o + checa a existencia
open('C:\\Users\\50s\\Desktop\\criandoarquivo2.txt', 'a') # APPEND apenas atualiza
