import datetime
import csv
import os.path
 

now = datetime.datetime.now()
hours = now.strftime("%H:%M")
argumento = str(input ('Qual o argumento? '))

if not os.path.exists("log.csv"):
    f  = open ('log.csv','w+')
    f.write("sep=\t\n")

f  = open ('log.csv','a')
f.write(f'{hours}\t')
f.write(f'{argumento}\n')

f.close()