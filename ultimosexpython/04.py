frase = input("Digite uma frase: ")
apoio = ""

for palavra in frase:

    if palavra == " ":
        apoio = apoio + "#"
    else:
        apoio = apoio + palavra

frase = apoio

print(frase)