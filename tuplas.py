import pandas as pd
#uma tupla é imutável
var = ('jetta','passat', 'gol', 'santana',('jipe', 'sandero', 'megane'))
val = (1000,2000,3000,4000,(1001,2001,3001))
#dessa forma mostra dentro da tupla seu local de referência
b=var[1]
#dessa forma mostra o ultimo elemento da tupla
c = var[-1]
#se eu  quiser mostrar elemento separados, nesse ele mostra o elemento 1 depois do : 2 ele mostra 1 se for:3 ele mostra 2 e assim por diante
d = var[0:2]
# se eu quiser ver um elemento da segunda tupla
e = var[-1][2]
#mostrar elemento da tupla principal e elemento da tupla interna
f = var[1],var[-1][1]
#mostra elementos dentro de elementos
g=var[0][1]
#como desmembrar tupla e colocar em variaveis diferentes (desempacotar)
item1, iten2, item3, item4, item5 = var
#colocar alguns elementos e outras variáveis
_,nom1, _, _, nom2=var
#juntar duas variaveis com dados congruentes
h = list(zip(var,val))
#varrer dentro da variável
for item in var:
    print()
#varrer dentro das duas variáveis e deixa tudo junto
for x in zip(var,val):
    print()
#separar os elementos com for (desempacotar)
for var, val in zip(var,val):
    print()
#colocar condição para varrer as variáveis
var1 = ('jetta','passat', 'gol', 'santana')
val1 = (1000,2000,3000,4000)
for var1, val1 in zip(var1,val1):
    if (val1>1000):
        print(var1)


