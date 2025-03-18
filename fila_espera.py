"""
Um programa para registrar os nomes dos clientes em espera e de cada vez retirar  primeiro nome a chegar 
Menu: 1.Entrada 2.Saída 3.Consultar Fila 4.Terminar
"""
import numpy as np
import Utils as utl

def entrada_clientes(fila,MAX_FILA,proximo):
    #Função responsavel pela entrada dos clientes no restaurante
    if proximo==MAX_FILA:#Verifica se a fila esta cheia
        print("A fila esta cheia")
        return proximo #Sai da função caso a fila estiver cheia
    fila[proximo]=utl.Ler_Nome_Litimes(1,50,"Nome proximo cliente: ")#Adiciona um cliente no em ultimo lugar da fila
    proximo+=1 #Aumenta a fila, informando a posiçao do proximo que deve entrar
    return proximo

def saida_clientes(fila,proximo,MAX_FILA):               
    #Função responsavel pela saida de clientes do restaurante
    if proximo==0: #Verifica se a fila esta vazia
        print("A fila esta Vazia")
        return proximo #Sai da função 
    print(f"O/A {fila[0]} entrou no restaurante.") #Informa qual cliente entrou no restaurante
    for k in range(proximo-1):
        fila[k]=fila[k+1]  #Muda a posição dos clientes na fila. ex: o segundo passa a ser o primeiro, o terceiro passa a ser o segundo
    fila[MAX_FILA-1]=""     # Remove o ultimo da fila, sem esta linha casa a fila estivesse cheia iria permanecer o ultimo nome na fila                        
    proximo-=1 # Informa o local onde o proximo da fila deve entrar
    return proximo

def consultar(fila,proximo,MAX_FILA):
    #Função responsavel por mostrar os clientes que estão na fila
    if proximo==0:  #Verifica se a fila esta Vazia
        print("A fila esta Vazia")
    else:
        print("Fila:")
        for i in range(proximo): #Cilclo para percorre a fila e mostrar a ordem e os clientes presentes na fila
            print(f"{i+1}º da fila: {fila[i]}")
    if proximo==MAX_FILA:
        print("A fila está Cheia.")

def menu():
    op=22
    MAX_FILA=15
    proximo_fila=0
    fila=np.empty(MAX_FILA,"U50")
    while op!=4: 
        op=utl.Ler_Inteiro_Limites(1,4,"1.Entrada\n2.Saída\n3.Consultar\n4.Terminar\n: ")
        if op==1:
            proximo_fila=entrada_clientes(fila,MAX_FILA,proximo_fila)
        elif op==2:
            proximo_fila=saida_clientes(fila,proximo_fila,MAX_FILA)
        elif op==3:
            consultar(fila,proximo_fila,MAX_FILA)

def main():
    menu()

if __name__=="__main__":
    main()