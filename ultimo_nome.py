def mudar_ordem(nome):
    nomes=nome.split()
    if len(nomes)>1:
        unome=f"{nomes[len(nomes)-1]}, "
        for i in range(len(nomes)-1):
            unome+=nomes[i]+" "
        return unome.strip()
    return nome

def main():
    nome=input("Nome: ")
    ultimo_nome=mudar_ordem(nome)
    print(ultimo_nome)
  
if __name__=="__main__":
    main()