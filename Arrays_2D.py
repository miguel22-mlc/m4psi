import numpy as np

def Matriz1():
    #Criar Matriz (Com valores dentro)
    Matriz = np.array([[1,2,3],[3,5,0]])

    print(Matriz)
    print(f"Matriz [0,0] = {Matriz[0,0]}")
    print(f"Matriz [1,2] = {Matriz[1,2]}")

    #Nº Dimensões
    print(f"Função 'len' + 'Matriz' = {len(Matriz)}")

    #Nº Linhas
    print(f"Função 'shape[0]' = {Matriz.shape[0]} 'Nº Linhas'")
    #Nº Colunas
    print(f"Função 'shape[1]' = {Matriz.shape[1]} 'Nº Colunas'")

    #Mostrar todos os elementos da Matriz
    for L in range(2):
        for C in range(3):
            print(Matriz[L, C])

def Matriz2():
    """
    Definir uma matriz 5,3
    """

    Matriz = np.zeros((5,3), dtype="i")

    #Ciclo p/ percorrer a Matriz
    for L in range(Matriz.shape[0]):
        for C in range(Matriz.shape[1]):
            print(Matriz[L, C])

Matriz2()