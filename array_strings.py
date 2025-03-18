import numpy as np

#Definir um array para strings
"""
i - inteiros
f - reais
b - boleanos
s - strings
U - unicode strings
M - datetime
"""
nomes=np.empty(10,dtype="U20")
for i in range(len(nomes)):
    nomes[i]=input("Introduza o nome: ")
print(nomes)
