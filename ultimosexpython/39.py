def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]

    lista_esquerda = merge_sort(lista_esquerda)
    lista_direita = merge_sort(lista_direita)

    return merge(lista_esquerda, lista_direita)

def merge(lista_esquerda, lista_direita):
    lista_ordenada = []
    i = 0  
    j = 0  

    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            lista_ordenada.append(lista_esquerda[i])
            i += 1
        else:
            lista_ordenada.append(lista_direita[j])
            j += 1

    while i < len(lista_esquerda):
        lista_ordenada.append(lista_esquerda[i])
        i += 1

    while j < len(lista_direita):
        lista_ordenada.append(lista_direita[j])
        j += 1

    return lista_ordenada

lista = [12, 11, 13, 5, 6, 7]
print("Lista original:", lista)
print("Lista ordenada:", merge_sort(lista))