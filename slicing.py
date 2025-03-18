nome="Joaquim Silva"
nome_5_letras=nome[0:5:1]
print(nome_5_letras)
nome_5_letras=nome[:5:1]
print(nome_5_letras)

for i in range(len(nome)):
    if nome[i]==" ":
        primeiro_nome=nome[:i:1]
        sobrenome=nome[i+1:len(nome):1]
print(primeiro_nome)
print(sobrenome)

nome_invertido=nome[::-1]
print(nome_invertido)

nome_2_em_2_letras=nome[::2]
print(nome_2_em_2_letras)

print(nome[-1])#Ultima letra do nome

for i in range(len(nome)):
    nome_invertido=nome[::-1]
    if nome_invertido[i]==" ":
        sobrenome_invertido=nome_invertido[:i:1]
print(sobrenome_invertido)

import numpy as np

nomes=np.array(["Joaquim","Maria","Antonio","Augusto","Dinis"])

print(nomes[::-1])

print(nomes[len(nomes)-2:])

print(nomes[::2])