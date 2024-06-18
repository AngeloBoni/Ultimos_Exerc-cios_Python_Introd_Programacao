def contarChar(texto_contagem):
    texto_aux = ""
    frequencia = {}

    for palavra in texto_contagem:
        if palavra in frequencia:
            frequencia[palavra] +=1
        else:
            frequencia[palavra] = 1

    for palavra in texto_contagem:
        if not(palavra in texto_aux):
            texto_aux += palavra + str(frequencia[palavra])
            
    return texto_aux


texto_contagem = input("Digite algo: ")

texto_contagem = contarChar(texto_contagem)

print(texto_contagem)