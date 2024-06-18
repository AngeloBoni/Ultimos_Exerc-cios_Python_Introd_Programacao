def calcularDeterminante(matriz):

    produto_principal = 1
    produto_secundaria = 1

    for i in range(len(matriz)):
        produto_principal *= matriz[i][i]
        produto_secundaria *= matriz[i][len(matriz) - 1 - i]

    return produto_principal - produto_secundaria

matriz = [[5, 6],
          [7, 8]]

print(calcularDeterminante(matriz))
            