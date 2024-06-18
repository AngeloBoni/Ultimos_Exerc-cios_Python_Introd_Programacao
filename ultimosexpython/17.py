texto = input("Digite um texto: ").lower()
texto = texto.split()

dic = {"vc": "você", "obg": "obrigado", "pprt": "papo reto", "amg": "amigo", "td" : "tudo"}

textoaux = ""

for palavra in texto:
    if palavra in dic:
        textoaux += " " + dic[palavra]
    else:
        textoaux += " " + palavra

texto = textoaux

print(texto)