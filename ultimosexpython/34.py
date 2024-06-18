def ordenarCrescente(lista):

    aux = 0

    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

ordenarCrescente(numeros)
print("Lista ordenada:", numeros)