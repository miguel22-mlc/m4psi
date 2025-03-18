import numpy as np
import Utils as utl

def mais_caro(valor,ncliente):
    """
    Função que recebe um array e seu tamanho e descobre o maior valor dentro do array e devolve sua posição dentro dele
    """
    posicao=0
    for n in range(1,ncliente):
        if valor[n]>valor[posicao]:
            posicao=n
    return posicao

def ler_dados(nome,valor,ncliente):
    for i in range(ncliente):
        nome[i]=utl.Ler_Nome_Litimes(1,50,f"Introduza o nome do {i+1}º cliente do dia: ")
        valor[i]=utl.Ler_Decimal(f"Introduza quanto que o {i+1}º cliente gastou: ")

def menu():
    NR_CLIENTES=utl.Ler_Inteiro_Limites(1,None,"Introduza a quantidade de clientes que entraram na loja hoje: ")
    nome_clientes=np.zeros(NR_CLIENTES,dtype="U51")
    valor_gasto=np.empty(NR_CLIENTES,dtype="f")
    ler_dados(nome_clientes,valor_gasto,NR_CLIENTES)
    cliente_caro=mais_caro(valor_gasto,NR_CLIENTES)
    print(f"O nome do cliente que mais gastou na loja hoje é {nome_clientes[cliente_caro]}.")

def main():
    menu()

if __name__=="__main__":
    main()



