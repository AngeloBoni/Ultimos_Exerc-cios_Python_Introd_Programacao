def verificarPrimo(numero):

    contador = 0

    for i in range(1, numero, 1):
        if numero % i == 0:
            contador += 1
            
    if contador > 1:
        return False
    else:
        return True

Primo = int(input("Qual número você deseja verificar se é primo?: "))

resultado = verificarPrimo(Primo)

print(f"O número {Primo} é primo?: {resultado}")