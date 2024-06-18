def removerDoTexto(texto):
    acentos ={ 'á': 'a', 'ã': 'a', 'â': 'a', 'à': 'a', 'ä': 'a',
        'é': 'e', 'ê': 'e', 'è': 'e', 'ë': 'e',
        'í': 'i', 'î': 'i', 'ì': 'i', 'ï': 'i',
        'ó': 'o', 'õ': 'o', 'ô': 'o', 'ò': 'o', 'ö': 'o',
        'ú': 'u', 'û': 'u', 'ù': 'u', 'ü': 'u',
        'ç': 'c'
        }
    especiais = [".", ",", "!", "?", "(", ")", "{", "}", "@", "#", "%", "+", "=", "~", ";", ":"]

    texto_aux = ""

    for caractere in texto:
        if caractere in acentos:
            texto_aux = texto_aux + acentos[caractere]
        elif caractere in especiais:
            texto_aux = texto_aux + " nulo "
        else:
            texto_aux = texto_aux + caractere

    return texto_aux


texto = input("Digite o texto: ").lower()

texto = removerDoTexto(texto)

print(texto)