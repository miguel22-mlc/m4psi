texto="Ola Mundo"
print(texto)

tamanho=len(texto)
print(tamanho)

texto=texto.upper()
print(texto)

texto=texto.lower()
print(texto)

texto=texto.capitalize()
print(texto)

texto=texto.strip()
print(texto)

texto=texto.replace(" ","_")
print(texto)

texto=texto.isdigit() #devolve verdadeiro ou falso se a string so tiver numeros verdadeiro 
print(texto)

frase="Ola Mundo, o computador é uma torradeira"

palavras=frase.split()
print(palavras)
print(len(palavras))
print(palavras[1])

posicao=frase.index("")
print(posicao)

posicao=frase.find("m")
if posicao==-1:
    print("Letra não foi encontrada na frase")
else:
    print(f"Encontrei a letra na posição {posicao}")

codigo=ord("a")
print(codigo)

letra=chr(codigo)
print(letra)