def fatorial(numero):
    contador = 1
    for i in range(numero, 0, -1):
        contador = contador * i

    return contador

inteiro = int(input("Receba um número: "))

print(f"O valor de {inteiro}! é: {fatorial(inteiro)}")
