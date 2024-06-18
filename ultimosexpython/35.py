def calcularMedia(lista):
    numeros = 0
    contador = 0

    for i in range(len(lista)):
        numeros += lista[i]
        contador += 1

    media = numeros / contador
    return media

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"A lista é: {lista}")
print(f"A média dessa lista é: {calcularMedia(lista)}")