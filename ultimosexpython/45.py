def verificarMatriz(matriz):
    soma_coluna = []
    soma_linha = []

    soma_diagonal_p = 0
    soma_diagonal_s = 0

    soma_aux = 0

    for linha in matriz:
        if len(linha) != len(matriz):
            return False



    for i in range(len(matriz)):
        soma_aux = 0
        for j in range(len(matriz)):
            soma_aux += matriz[j][i]
        soma_coluna.append(soma_aux)

    for i in range(len(matriz)):
        soma_aux = 0
        for j in range(len(matriz)):
            soma_aux += matriz[i][j]
        soma_linha.append(soma_aux)

    for i in range(len(matriz)):
        soma_diagonal_p += matriz[i][i]

    for i in range(len(matriz)):
        soma_diagonal_s += matriz[i][len(matriz) - 1 - i]

    
    referencia = soma_linha[0]

    for i in range(len(matriz)):
        if soma_linha[i] != referencia or soma_coluna[i] != referencia:
            return False

    if soma_diagonal_p != referencia or soma_diagonal_s != referencia:
        return False

    return True

matriz = [[2, 7, 6, 4], [9, 5, 1, 10], [4, 3, 8, 10]]

print(verificarMatriz(matriz)) 