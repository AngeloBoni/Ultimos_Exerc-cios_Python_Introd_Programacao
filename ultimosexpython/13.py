frase = input("Digite uma frase: ")
frase = frase.lower()
cont = []

for i in range(6):
    cont.append(0)

for char in frase:
    if char == " ":
        cont[0] += 1
    elif char == "a":
        cont [1] += 1
    if char == "e":
        cont[2] += 1
    elif char == "i":
        cont [3] += 1
    if char == "o":
        cont[4] += 1
    elif char == "u":
        cont [5] += 1

print(f"Nessa frase existem: \n Espaços em branco: {cont[0]} \n Letras a's: {cont[1]}\n Letras e's: {cont[2]} \n Letras i's: {cont[3]} \n Letras o's: {cont[4]} \n Letras u's: {cont[5]} ")

