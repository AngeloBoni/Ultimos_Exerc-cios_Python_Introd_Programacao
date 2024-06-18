def verificarPrimos(numero):
    contador = 0

    for i in range(1, numero, 1):
        if numero % i == 0:
            contador += 1
            
    if contador > 1:
        return False
    else:
        return True

def gerarPrimos(n):
    primos = []
    numero = 2

    while len(primos) < n:
        if verificarPrimos(numero):
            primos.append(numero)
        numero += 1
        
    
    return primos

n = int(input("Quantos números primos você deseja exibir?: "))

print(gerarPrimos(n))
