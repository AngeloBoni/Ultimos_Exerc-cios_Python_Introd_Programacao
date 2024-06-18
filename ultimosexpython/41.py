def removerElementos(lista):
    lista_aux = []
    for elemento in lista:
        if not(elemento in lista_aux):
            lista_aux.append(elemento)

    return lista_aux

lista = [1,11, 1, 2, 3, 5, 4, 5, 3]

print(f"Lista original: {lista}")
print(f"Lista modificada: {removerElementos(lista)}")





