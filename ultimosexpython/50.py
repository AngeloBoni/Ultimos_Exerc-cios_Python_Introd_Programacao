def transformarNumerosRomanos(numero_romano):

    guardar_valor = {"I": 1, "V" : 5, "X" : 10, "L" : 50,
                     "C" : 100, "D" : 500, "M" : 1000}
    numero_final = 0
    
    for i in range(len(numero_romano)):
        if (i != len(numero_romano) - 1) and (guardar_valor[numero_romano[i]] < guardar_valor[numero_romano[i + 1]]):
            numero_final -= guardar_valor[numero_romano[i]]
        else:
            numero_final += guardar_valor[numero_romano[i]]


    return numero_final

numero = input("Digite seu número romano: ").upper()

print(transformarNumerosRomanos(numero))
