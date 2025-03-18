def Ler_Inteiro(Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que lê do utilizador um número inteiro.
    Também garante que o valor inserido é válido.
    """

    while True:
        Dados = input(Mensagem)

        if len(Dados) == 0:
            continue

        #Verificar se existe um - no inicio da String
        if Dados[0] == "-":
            Testar = Dados.replace("-", "")

        else:
            Testar = Dados

        if Testar.isdigit():
            return int(Dados)
        print("\nErro: O valor inserido não é válido⚠️ \n")


def Ler_Inteiro_Limites(Min, Max=None, Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que recebe o valor Min e Max a ler do utilizador.
    A função devolve o valor quando é um inteiro válido.
    """

    while True:
        X = Ler_Inteiro(Mensagem)

        if Max == None or Min == None or (X >= Min and X <= Max):
            return X
        print("\nErro: O valor inserido não é válido⚠️ \n")
        

def Ler_Decimal(Mensagem="Introduza um valor inteiro: "):
    """
    Função que lê do utilizador um número decimal.
    Também garante que o valor inserido é válido e aceita como separador das casas decimais . ou , .
    """
    
    while True:
        Dados = input(Mensagem)

        if len(Dados) == 0:
            continue

        #Substituir , por .
        Dados = Dados.replace(",", ".")

        #Verificar se existe um - no inicio da String
        if Dados[0] == "-":
            Testar = Dados.replace("-", "")

        else:
            Testar = Dados

        #Contar os pontos decimais
        Pontos = Testar.count(".")

        #remover os pontos decimais
        Testar = Testar.replace(".", "")

        #Não pode ter mais de 1 ponto decimal e só pode ter digitos
        if Testar.isdigit() and Pontos <= 1:
            return float(Dados)
        print("\nErro: O valor inserido não é válido⚠️  \n")

def Ler_Decimal_Limites(Min, Max=None, Mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que recebe o valor Min e Max a ler do utilizador.
    Também garante que o valor inserido é válido e aceita como separador das casas decimais . ou , .
    """

    while True:
        X = Ler_Decimal(Mensagem)

        if Max == None or (X >= Min and X <= Max):
            return X
        print("\nErro: O valor inserido não é válido⚠️ \n")
        
def Ler_Nome_Litimes(Min, Max=None, Mensagem="Introduza uma palavra: "):
    """
    Função que recebe o valor Min e Max de letras a ler do utilizador.
    Também garante que a palavra inserido é válido.
    """

    while True:
        Nome = input(Mensagem)
        if (Min == None and len(Nome) <= Max) or (Max == None and len(Nome) >= Min) or (len(Nome) >= Min and len(Nome) <= Max):
            return Nome
###############################################################################################################################
