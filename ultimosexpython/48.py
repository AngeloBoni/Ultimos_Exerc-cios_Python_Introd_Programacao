def verificarPangrama(string):
    letras ={"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" :0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0,
             "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v": 0,
             "w" : 0, "x" : 0, "y" : 0, "z": 0
             }
    
    contagem = 0
    
    for caractere in string:
        if caractere in letras:
            letras[caractere] += 1

    for caractere in letras:
        if letras[caractere] > 0:
            contagem += 1
    
    if contagem >= 26:
        return True
    else:
        return False
    
frase = input("Digite seu pangrama: ").lower()

print(verificarPangrama(frase))