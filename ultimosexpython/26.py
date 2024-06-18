def calcularArea(tipo, v1, v2 = 0, l1 = 0, l2 = 0, l3 = 0):
    if tipo == 0:
        area = v1 ** 2 * 3.14
        perimetro = 2 * 3.14 * v1
    elif tipo == 3:
        area = (v1 * v2)/2
        perimetro = l1 + l2 + l3
    elif tipo == 4:
        area = v1 * v2
        perimetro = v1 * 2 + v2 * 2
    
    retorno_duplo = (f"Área: {area}\nPerímetro: {perimetro}")
    return retorno_duplo

figura = int(input("Quantos lados tem a figura? (4 para retângulo, 3 para triângulo e 0 para circunferência): "))
validacao = False
resultado = ""

while validacao == False:
    if figura == 0:
        validacao = True
        raio = float(input("Digite o raio do círculo: "))
        resultado = calcularArea(0, raio)
    elif figura == 3:
        validacao = True
        validacaoT = False
        l1 = float(input("Digite o primeiro lado do triângulo: "))
        l2 = float(input("Digite o segundo lado do triângulo: "))
        l3 = float(input("Digite o terceiro lado do triângulo: "))

        while validacaoT == False:
            if not(abs(l2 - l3) < l1 < l2 + l3) and (abs(l1 - l3) < l2 < l1 + l3) and (abs(l1 - l2) < l3 < l1 + l2):
                validacaoT = False
                print("Valores não formam um triângulo, favor, repetir: ")
                l1 = float(input("Digite o primeiro lado do triângulo: "))
                l2 = float(input("Digite o segundo lado do triângulo: "))
                l3 = float(input("Digite o terceiro lado do triângulo: "))
            else:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                validacaoT = True
                resultado = calcularArea(3, base, altura, l1, l2, l3)

    elif figura == 4:
        validacao = True
        l1 = float(input("Digite a base do retângulo: "))
        l2 = float(input("Digite a altura do retângulo: "))
        resultado = calcularArea(4, l1, l2)
    else:
        print("Valor inválido")
        figura = int(input("Quantos lados tem a figura? (4 para retângulo, 3 para triângulo e 0 para circunferência): "))

print(resultado)