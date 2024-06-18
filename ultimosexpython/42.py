def verificarSubsequencia(subseq, string):
    
    validacao = False

    cont_aux = 0

    for i in range(len(string)):
        if(cont_aux < len(subseq) and string[i] == subseq[cont_aux]):
            cont_aux += 1

        if cont_aux == len(subseq):
            return True
        
    return False

print(verificarSubsequencia("abc", "abcde"))
print(verificarSubsequencia("cab", "abcde"))
print(verificarSubsequencia("abd", "abcde"))
print(verificarSubsequencia("abe", "abcde"))
print(verificarSubsequencia("Wac", "abcde"))
