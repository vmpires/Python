compra = 'segunda'
prazo = 5
semana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado','domingo','segunda','terca','quarta','quinta','sexta']
compra_n = semana.index(compra)
entrega = semana[compra_n+prazo]

if prazo == 0:
    print ('chega hoje!')
else:
    print (f'sera entregue {entrega}')






