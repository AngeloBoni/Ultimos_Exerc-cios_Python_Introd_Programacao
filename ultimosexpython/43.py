def encontrarInterseccao(lista1, lista2):
    lista_Aux = []
    for elemento in lista1:
        if (elemento in lista1 and elemento in lista2) and not(elemento in lista_Aux):
            lista_Aux.append(elemento)
        
    return lista_Aux

numeros = [5, 1, 2, 3, 4,9, 5, 3, 1]
numeros01 = [0, 1,5,6,2, 5, 2, 3, 6]

lista = encontrarInterseccao(numeros, numeros01)

print(lista)