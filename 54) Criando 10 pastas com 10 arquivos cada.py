import os
import platform
import shutil
from distutils.dir_util import copy_tree

diretorio = 'C:\\Users\\50s\\Desktop\\10pastas'

if not os.path.exists(diretorio):
    os.mkdir(diretorio)

for i in range(1,11):
    if not os.path.exists(diretorio+'\\pasta_'+str(i)):
        os.mkdir(diretorio+'\\pasta_'+str(i))
    for f in range(1,11):
        open(diretorio + '\\pasta_' + str(i) + '\\arquivo_' + str(f) + '.txt', 'w+')
