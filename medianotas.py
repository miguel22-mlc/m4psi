import numpy as np

def acimamedia(media,alunos,notas):
    for n in range(alunos):
        if notas[n]>media:
            print(f"A nota {notas[n]} do aluno nº{n+1} é acima da média")


def mediaalunos(soma,alunos):
    media=soma/alunos
    print(f"A média dos alunos é {media}")
    return media

def main():
    NR_ALUNOS=10
    soma=0
    notas=np.zeros(NR_ALUNOS)
    for n in range(NR_ALUNOS):
        notas[n]=int(input(f"Introduza a nota do aluno nº{n+1}: "))
        soma+=notas[n]
    media= mediaalunos(soma,NR_ALUNOS)
    acimamedia(media,NR_ALUNOS,notas)
if __name__=="__main__":
    main()