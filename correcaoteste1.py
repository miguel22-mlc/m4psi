import numpy as np
nomes=input("Nomes: ")
tempo=input("tempo: ")
pilotos=np.array(nomes.split(", "))
voltas=np.array(tempo.split(", "))
p=0
while p<5:
    if int(voltas[p])<0:
        voltas[p]=int(input(f"O numero deve ser positivo, introduza de novo: "))
    else:
        p+=1
pm=0
pp=0
for i in range(1,5):
    if int(voltas[i])<int(voltas[pm]):
        pm=i
    if int(voltas[i])>int(voltas[pp]):
        pp=i
diferenca=int(voltas[pp])-int(voltas[pm])
print(f"Primeiro Lugar: {pilotos[pm]}\nÚltimo Lugar: {pilotos[pp]}\nDiferença: {diferenca} minutos")
print("Nomes e Tempo gastos pelos pilotos")
for i in range(5):
    print(f"{pilotos[i]}: {voltas[i]} minutos")