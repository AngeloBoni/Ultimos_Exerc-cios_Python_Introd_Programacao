StringAntiga = input("Digite a primeira String: ")
StringNova = input("Digite a segunda string: ")

StringAntiga = StringAntiga.split(" ") 

x = len(StringAntiga)

StringAntiga[x-1] = StringNova
Exibida = ""

for palavras in StringAntiga:
    if(palavras == StringAntiga[0]):
        Exibida = Exibida + palavras
    else:
        Exibida = Exibida + " " + palavras

print(Exibida)