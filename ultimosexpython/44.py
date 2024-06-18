def calcularPotencia(base, expoente):
    
    resultado = 1
    
    for i in range(expoente):
        resultado *= base

    return resultado

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(f"{base} elevado a {expoente} é: {calcularPotencia(base, expoente)}")