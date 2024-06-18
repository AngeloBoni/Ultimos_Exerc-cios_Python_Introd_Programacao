def Manipular(texto):

    texto_pontuacao = ""

    for palavra in texto:
        if not((palavra == ".") or (palavra == ",")):
            texto_pontuacao += palavra
    
    texto = texto_pontuacao.split(" ")

    frequencia = {}
    for palavra in texto:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    
    return frequencia


texto_usuario = input("Digite o texto: ").lower()
frequencia = Manipular(texto_usuario)
print(frequencia)
