import Utils as utl

def ordenar(matriculas,tempo):
    pass
    

def verificar_repetidas(matriculas):
    repetidas=""
    for i in range(len(matriculas)):
        for n in range(len( matriculas)):
            if i!=n and matriculas[i]==matriculas[n]:
                if matriculas[i] not in repetidas:
                    repetidas+=f"|{matriculas[i]}| "
    return repetidas
        
def acima_media(matriculas,tempo,media):
    acima_media=""
    for i in range(len(tempo)):
        if media<int(tempo[i]):
            acima_media+=f"|{matriculas[i]}| "
    return acima_media

def media_tempo(tempo):
    soma=0
    for i in range(len(tempo)):
        soma+=int(tempo[i])
    media=soma/len(tempo)
    return media

def mais_tempo(tempo):
    maior=int(tempo[0])
    posicao=0
    for i in range(1,len(tempo)):
        if maior<int(tempo[i]):
            maior=int(tempo[i])
            posicao=i
    return posicao

def verificacao(matriculas,tempo):
    if len(matriculas)==len(tempo):
        return True
    return False

def pedir_tempo():
    tempo=utl.Ler_Nome_Litimes(1,None,"Introduza o tempo em que cada carro esteve estacionado(segundos)\nNa ordem em que as matriculas foi inserida: ")
    tempo=tempo.split(",")
    return tempo

def pedir_matriculas():
    matriculas=utl.Ler_Nome_Litimes(1,None,"Introduza as matriculas dos carros que estiveram estacionados\nMatriculas separadas por virgulas: ")
    matriculas=matriculas.split(",")
    return matriculas

def menu():
    matriculas=pedir_matriculas()
    tempo=pedir_tempo()
    if verificacao(matriculas,tempo):
        posicao=mais_tempo(tempo)
        media=media_tempo(tempo)
        a_media=acima_media(matriculas,tempo,media)
        repetidas=verificar_repetidas(matriculas)
        print(f"\nO carro de matricula |{matriculas[posicao]}| foi oque ficou mais tempo estacionado.\nA media de tempo no estacionamento é {media}segundos\nOs carros acima da media de tempo são {a_media}\n")
        if repetidas!= "":
            print(f"Os carros que estacionaram mais de uma vez foram {repetidas}.")
    else:
        print("Dados invalidos.")

def main():
    menu()

if __name__=="__main__":
    main()