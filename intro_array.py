import numpy as np

numeros=np.array([10,14,-5,33,120])

for i in range (5):
    numeros[i]=0


array_0d=np.array(40)

print(type(numeros))
print(type(array_0d))
print(array_0d)
print(numeros.ndim)

for x in numeros:
    print(x)

for x in range(len(numeros)):
    print(numeros[x])

    #Cirar um array vazio

vazio=np.empty(10)
print(vazio)
zeros= np.zeros(10)
print(zeros)