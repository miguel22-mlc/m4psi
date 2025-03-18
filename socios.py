import numpy as np
socios_a=np.array(["Joaquim","Maria","João"])
socios_b=np.array(["Maria","Antonio","Carla"])
for i in range (len(socios_a)):
    if socios_a[i] in socios_b:
        print(f"O socio de nome {socios_a[i]} é socio de ambos os clubes ")