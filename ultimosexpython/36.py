def contarNumeroPalavras(texto):
    
    texto = texto.split()
    contador = 0

    for palavra in texto:
        contador += 1
    
    return contador

texto_entrada = input("Digite um texto para ser feita a contagem de palavras: ")

print(f"O texto possui: {contarNumeroPalavras(texto_entrada)} palavras")