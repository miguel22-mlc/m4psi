import numpy as np
import Utils as utl

def adicionar(nomes,telefones,emails,posicao,MAX):
    if posicao==MAX:
        print("|Agenda Cheia|")
        return posicao
    nomes[posicao]=utl.Ler_Nome_Litimes(1,50,"Nome: ")
    telefones[posicao]=utl.Ler_Nome_Litimes(1,15,"Telefone: ")
    emails[posicao]=utl.Ler_Nome_Litimes(1,50,"Email: ")
    posicao+=1
    return posicao

def listar(nomes,telefones,emails,posicao):
    print("\t\t  |Contatos|")
    for i in range(posicao):
        print(f"\tNome: {nomes[i]} | Telefone: {telefones[i]} | Email: {emails[i]}")
    
def procurar(nomes,telefones,emails,posicao):
    nome=utl.Ler_Nome_Litimes(1,50,"Introduza o nome do contato que deseja encontrar: ")
    for i in range (posicao):
        if nome in nomes[i]:
             print(f"\tNome: {nomes[i]} | Telefone: {telefones[i]} | Email: {emails[i]}")

def editar(nomes,telefones,emails,posicao):
    edita=utl.Ler_Nome_Litimes(1,50,"Qual contato deseja editar: ")
    for i in range(posicao):
        if edita in nomes[i]:
            op=input(f"Deseja editar este contato: {nomes[i]} | {telefones[i]} | {emails[i]}\n(S/N): ")
            if op.upper()=="S":
                print("Caso não queira editar alguma opção deixe em branco")
                novo_nome=utl.Ler_Nome_Litimes(0,50,"Novo nome: ")
                novo_telefone=utl.Ler_Nome_Litimes(0,50,"Novo telefone: ")
                novo_emails=utl.Ler_Nome_Litimes(0,50,"Novo email: ")
                if novo_nome!="":
                    nomes[i]=novo_nome
                if novo_emails!="":
                    emails[i]=novo_emails
                if novo_telefone!="":
                    telefones[i]=novo_telefone
                break

def apagar(nomes,telefones,emails,posicao,MAX):
    listar(nomes,telefones,emails,posicao)
    apaga=utl.Ler_Nome_Litimes(1,50,"\t\t|Apagar Contato|\nIntroduza um nome: ")
    for i in range(posicao):
        if apaga in nomes[i]:
            if i==MAX-1:
                nomes[MAX-1]=""
                telefones[MAX-1]=""
                emails[MAX-1]=""
                break
            op=utl.Ler_Nome_Litimes(1,1,f"Tem certeza de que deseja apagar este contato:\nNome: {nomes[i]} | Telefone: {telefones[i]} | Email: {emails[i]}\nS.sim\nN.não\n:")
            if op.lower()=="s":
                for k in range(i,posicao):
                    nomes[k]=nomes[k+1]                 
                    telefones[k]=telefones[k+1]
                    emails[k]=emails[k+1]
    posicao-=1
    return posicao
            
def menu():
    MAX_CONTATOS=100
    nomes=np.empty(MAX_CONTATOS,"U50")
    telefones=np.empty(MAX_CONTATOS,"U15")
    emails=np.empty(MAX_CONTATOS,"U50")
    p=0
    op=22
    while op!=6:
        op=utl.Ler_Inteiro_Limites(1,6,"Escolha oque deseja realizar:\n1.Adicionar\n2.Listar Todos\n3.Proucurar\n4.Editar\n5.Apagar\n6.Terminar\n:")
        if op==1:
           p= adicionar(nomes,telefones,emails,p,MAX_CONTATOS)
        elif op==2:
            listar(nomes,telefones,emails,p)
        elif op==3:
            procurar(nomes,telefones,emails,p)
        elif op==4:
            editar(nomes,telefones,emails,p)
        elif op==5:
            print(nomes)
            p=apagar(nomes,telefones,emails,p,MAX_CONTATOS)
            print(nomes)
        
def main():
    menu()

if __name__=="__main__":
    main()