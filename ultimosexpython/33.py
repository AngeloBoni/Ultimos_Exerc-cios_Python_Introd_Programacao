def contarVogais(texto):
    contador = 0

    for char in texto:
        if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
            contador += 1

    return contador

texto_entrada = input("Digite um texto: ").lower()

vogais = contarVogais(texto_entrada)

print(f"O texto possui {vogais} vogais")