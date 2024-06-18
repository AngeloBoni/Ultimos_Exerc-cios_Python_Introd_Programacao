def texto_censurado(texto, palavras):

    texto_separado = texto.split()
    textoaux = ""

    for i in texto_separado:
        if i in palavras:
            textoaux = textoaux + " " + "*" * len(i)
        else:
            textoaux = textoaux + " " + i
    return textoaux

texto = input("Digite seu texto: ")
palavras = input("Quais palavras devem ser censuradas? (Separe por espaços -> exemplo: pão paz terra):")

palavras = palavras.split()

texto = texto_censurado(texto, palavras)

print(f"Novo texto:\n{texto}")