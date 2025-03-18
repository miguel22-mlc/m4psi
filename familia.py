import Utils as utl

def verificar_familia(nome1,nome2):
    nome1=nome1.split()
    nome2=nome2.split()
    for i in nome1[1::1]:
        if i in nome2[1::1]:  #Compara os sobrenomes das pessoas para ver se são da mesma família
            return f"{nome1[0]} e {nome2[0]} são da mesma família, {i} "   
    return("Eles não são da mesma família")

def main():
    nome1=utl.Ler_Nome_Litimes(1,None,"Nome 1: ")
    nome2=utl.Ler_Nome_Litimes(1,None,"Nome 2: ")
    familia=verificar_familia(nome1,nome2)
    print(familia)
if __name__=="__main__":
    main()

