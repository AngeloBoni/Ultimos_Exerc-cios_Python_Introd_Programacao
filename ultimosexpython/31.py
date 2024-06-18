def gerarFibonacci(quantidade):
    atual = 0
    anterior = 0
    resultado = 1

    while(quantidade != 0):
        print(resultado)
        anterior = atual
        atual = resultado
        resultado = anterior + atual
        quantidade -= 1

    return "Resultado gerado a cima"


sequencia = int(input("Quantos números você deseja gerar na sequência?: "))

print(gerarFibonacci(sequencia))