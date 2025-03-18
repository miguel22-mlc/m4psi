import numpy as np
import Utils as utl

ELEMENTOS=utl.Ler_Inteiro("Introduza quantos elementos o array deve ter: ")
nomes=np.empty(ELEMENTOS,dtype="U100")

for i in range(ELEMENTOS):
    nomes[i]=input("Introduza um nome: ")
print(nomes)

for n in range(ELEMENTOS//2):
    ELEMENTOS-=1
    temp=nomes[n]
    nomes[n]=nomes[ELEMENTOS]
    nomes[ELEMENTOS]=temp
print(nomes)