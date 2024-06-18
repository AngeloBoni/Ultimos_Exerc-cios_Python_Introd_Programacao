Palavra01 = input("Digite a primeira palavra: ").upper()
Palavra02 = input("Digite a segunda palavra: ").upper()

condicao = True

if len(Palavra01) != len(Palavra02):
    print("Não são anagramas")
else:
    if sorted(Palavra01) == sorted(Palavra02):
        print("São anagramas")
    else:
        print("Não são anagramas")