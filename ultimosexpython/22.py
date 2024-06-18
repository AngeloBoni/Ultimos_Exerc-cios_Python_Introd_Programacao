def verificar_equilibrio(string):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for caractere in string:
        if caractere in pares.values():  
            pilha.append(caractere)
        elif caractere in pares.keys():  
            if pilha == [] or pares[caractere] != pilha.pop():
                return False
    
    return pilha == []

texto = input("Digite uma string para verificar se os parênteses estão equilibrados: ")
if verificar_equilibrio(texto):
    print("Os parênteses estão equilibrados.")
else:
    print("Os parênteses não estão equilibrados.")