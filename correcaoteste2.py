contar=0
email=input("email: ")
pp=input("pp: ")
if len(pp)>=8:
    contar+=1
if pp not in email:
    contar+=1
for l in pp:
    if l >="a" and l<="z":
        contar+=1
        break
for l in pp:
    if l >="A" and l<="Z":
        contar+=1
        break
for n in range(10):
    if str(n) in pp:
        contar+=1
        break
if contar==5:
    print("Senha segura")
else:
    print("Senha não segura")