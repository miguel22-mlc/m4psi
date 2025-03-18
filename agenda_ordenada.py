"""
Criar uma agenda que resgistra os nomes por ordem alfabetica.
Guardar o nome e a data de nascimento das pessoas ordenadas por ordem crescente aos nomes
Menu: 1.Adicionar Contatos 2.Listar Contatos 3.Pesquisas 4.terminar
"""
import numpy as np
import Utils as utl

def pesquisa(contatos,nome):
    primeiro=0
    ultimo=0
    for k in contatos:
        if k=="":
            break
        ultimo+=1

    while primeiro<=ultimo:
        meio=(primeiro+ultimo)//2
        valor_meio=contatos[meio]
        if nome == valor_meio:
            print(f"\n|{valor_meio}|")
            return
        elif valor_meio<nome:
            primeiro=meio+1
        else:
            ultimo=meio-1
    print("\nNome não existe.")

def listar(contatos,data_nascimento,contagem,MAX):
    if contagem==0:
        print("A lista está Vazia.")
        return
    print("\t|Lista Contatos|")
    for i in range(contagem):
        print(f"\n| Nome: {contatos[i]} | Data: {data_nascimento[i]} |")
    if contagem==MAX:
        print("\nA lista está cheia.")

def ordenar(contatos,data_nascimento,nova_data,contato_novo,contagem) :
    posicao=contagem
    if contagem==0:
        contatos[0]=contato_novo
        data_nascimento[0]=nova_data
        return
    for p in range(contagem):
        if contato_novo<contatos[p]:
            posicao=p
            break      
    for i in range(contagem,posicao,-1):
        contatos[i]=contatos[i-1]
        data_nascimento[i]=data_nascimento[i-1]
    contatos[posicao]=contato_novo
    data_nascimento[posicao]=nova_data

def adicionar(contatos,data_nascimento,MAX,contagem):
    if contagem==MAX:#Verifica se os contatos estão cheios
        print("Limite de Contatos Atingido")
        return contagem #Sai da função caso a fila estiver cheia
    contato_novo=utl.Ler_Nome_Litimes(1,50,"Novo Contato: ")#Adiciona um contato novo
    nova_data=utl.Ler_Nome_Litimes(1,50,f"Data de Nascimento de {contato_novo}: ")
    ordenar(contatos,data_nascimento,nova_data,contato_novo,contagem) 
    contagem+=1 #Aumenta a fila, informando a posiçao do proximo que deve entrar
    return contagem

def menu():
    op=22
    MAX_CONTATOS=15
    contagem_contatos=0
    data_nascimento=np.empty(MAX_CONTATOS,"U50")
    contatos=np.empty(MAX_CONTATOS,"U50")
    while op!=4:
        op=utl.Ler_Inteiro_Limites(1,4,"\n1.Adicionar Contatos\n2.Listar Contatos\n3.Pesquisar🔍\n4.Terminar\n: ")
        if op==1:
            contagem_contatos=adicionar(contatos,data_nascimento,MAX_CONTATOS,contagem_contatos)
        elif op==2:
            listar(contatos,data_nascimento,contagem_contatos,MAX_CONTATOS)
        elif op==3:
            nome=utl.Ler_Nome_Litimes(1,50,"Pesquisa🔍: ")
            pesquisa(contatos,nome)

def main():
    menu()

if __name__=="__main__":
    main()