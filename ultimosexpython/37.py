def converterBinarioDecimal(binario):
    soma = 0
    for numero in range(len(binario)):
        if binario[numero] == "1":
            soma += 1 * 2 ** (len(binario) - numero - 1)
        elif binario[numero] == "0":
            soma += 0
        else:
            return "Valor inválido inserido!"
           
    return soma
    


binario = input("Digite o número binário: ")

print(f"O número {binario} convertido de binário para decimal é: {converterBinarioDecimal(binario)} ")
