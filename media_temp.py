import numpy as np
import Utils as utl

def mediaa(temp_mm,meses):
    soma=0
    for i in range(meses):
        soma+=temp_mm[i]
    media=soma/meses
    return round(media,1)

def maiort(temp_mm,meses):
    maior=temp_mm[0]
    for i in range(1,meses):
        if temp_mm[i]>maior:
            maior=temp_mm[i]
    return maior

def menort(temp_mm,meses):
    menor=temp_mm[0]
    for i in range(1,meses):
        if temp_mm[i]<menor:
            menor=temp_mm[i]
    return menor

def acimamedia(media,temp_mm,meses):
    acimamedia=""
    for i in range(meses):
        if temp_mm[i]>media:
            acimamedia+=str(int(temp_mm[i]))+"°C "
    return acimamedia

def modat(temp_mm,meses):
    contarmoda=0
    for i in range(meses):
        teste=temp_mm[i]
        for n in range(meses):
            contar=0
            if teste==temp_mm[n]:
                contar+=1
            if contar>contarmoda:
                contarmoda=contar
                moda=temp_mm[n]
    return int(moda)

def menu():
    MESES=12
    temp_mm=np.zeros(MESES)
    for i in range(MESES):
        temp_mm[i]=utl.Ler_Inteiro(f"Introduza a média de temperatura do {i+1}º mês do ano: ")
    media_anual=mediaa(temp_mm,MESES)
    maior=maiort(temp_mm,MESES)
    menor=menort(temp_mm,MESES)
    moda=modat(temp_mm,MESES)
    acima_media=acimamedia(media_anual,temp_mm,MESES)
    print(f"A média de temperatura anual é {media_anual}°C\nA maior temperatura do ano foi {maior}°C e a menor é {menor}°C\nAs temperaturas acima da média são {acima_media}\nA moda das temperaturas é {moda}°C")

def main():
    menu()

if __name__=="__main__":
    main()