import numpy as np

'''km = np.loadtxt('carros-km.txt')
ano = np.loadtxt('carros-anos.txt', dtype=int)
km_media = km / (2019 - ano)
#print(ano)
#print(km_media)

carro = [
    'Jetta Variant', 
    'Motor 4.0 Turbo', 
    2003, 
    44410.0, 
    False, 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 
    88078.64
]
#print(carro)
b = "false" not in carro
c = '2003' in carro
a='rodas de liga' in  carro
print(a, b, c)
carro = [
    'Jetta Variant', 
    'Motor 4.0 Turbo', 
    'Rodas de liga', 'Travas elétricas', 'Piloto automático']
a=list(range(10))
for i in range(10):
    print(i**2)
dados = [ 
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]
result_2 = []
for lista in dados:
    result_2 += lista
print(result_2)

np_array = np.arange(1000000)
py_list = list(range(1000000))
inicio = time.time()
for _ in range(100): py_list = [x *2 for x in py_list]
fim = time.time()
for _ in  range(100):np_array *= 2

print(fim 9- inicio)'''
c= [0,1,2,3,4,5,6,7,8,9]
s = np.array(c)

cafe = 15+10+10+15+9+30+15+25+14
cost = 17+15+45+16+40
cafe1 = 30+15
alm = 60+15+45+16+20+120
hig = 30+12+35+50
total = cafe+cafe1+cost+alm+hig
percapt= total/27
print("iremos gastar no cafe =",cafe)
print("iremos gastar no costela =",cost)
print("iremos gastar no cafe =",cafe1)
print("iremos gastar no almoço =",alm)

print(total)
print(percapt)

