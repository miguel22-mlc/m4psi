"""
Programa para calcular e mostrar quantos carros ha da mesma marca sem repetir
"""

import numpy as np

Carros = np.array(["Tesla", "Volvo", "BMW", "Peugeot", "Tesla", "BYD", "Mercedes", "BYD"])
Vezes = np.zeros(len(Carros))

for i in range (len(Carros)):
    for j in range(i + 1, (len(Carros))):
        if Carros[i] == Carros[j]:
            for k in range(len(Carros)):
                if Carros[i] == Carros[k]:
                    Vezes[k] = Vezes[k] + 1
                    break

for i in range(len(Vezes)):
    if Vezes[i] != 0:
        print(f"O carro '{Carros[i]}' repete-se {Vezes[i]}")
    
