import matplotlib.pyplot as plt
import numpy as np

# Valores do gráfico
valores = np.array([20,60,5,15])

#Itens do Gráfico
mylabels = ['Maçãs','Bananas','Laranjas','Abacaxis']

# Espaço entre as fatias do gráfico
myexplode = [0,0,0,0]

# Monta o gráfico e exibe
plt.pie(valores, labels=mylabels, explode=myexplode)
plt.show()