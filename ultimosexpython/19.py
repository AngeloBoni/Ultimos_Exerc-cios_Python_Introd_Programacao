def inverterOrdem(texto):
    inversao = ""
    for i in range(len(texto)-1, -1, -1):
        inversao = inversao + " " + texto[i]

    return inversao


texto = input("Digite seu texto: ")
texto = texto.split(" ")

texto = inverterOrdem(texto)

print(texto)
