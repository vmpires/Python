## Payback in CSV ##
import math

def CalcularPayback(conta,valorsistema):   
    mesestotais = valorsistema/conta
    mesesarredondados = math.ceil(mesestotais)
    if mesesarredondados >= 12:
        anos = (mesesarredondados//12)
        mesesrestantes = mesesarredondados%12
        
        if mesesrestantes == 0:
            return str(f'{anos} anos')
        else:
            return str(f'{anos} anos e {mesesrestantes} meses')
    else:
        return str(f'{mesestotais} meses')

conta = []
csv  = open ('log.csv','r')
lines = csv.read().split('\n')

for line in lines:
    conta.append(line.split(';'))

f  = open ('log2.csv','w+')
for line in conta:
    payback = CalcularPayback(int(line[0]),int(line[1]))
    final = str(f'{line[0]};{line[1]};{payback}\n')
    f.write(final)
csv.close()
f.close()