def tirarespaços(PalavraBase):
    
    Auxiliar = ""
    for palavra in PalavraBase:

        if not(palavra == " "):
            Auxiliar += palavra
    return Auxiliar

def inverter(PalavraBase):
    Auxiliar = ""
    for i in range(len(PalavraBase)-1,  -1, -1):
        Auxiliar = Auxiliar + PalavraBase[i]
      
    return Auxiliar

PalavraBase = input("Digite a primeira palavra: ").upper()
PalavraPalindromo = input("Digite a segunda palavra: ").upper()

SAuxBase = tirarespaços(PalavraBase)

SAuxPalindromo = tirarespaços(PalavraPalindromo)
SAuxPalindromo = inverter(SAuxPalindromo)


if(SAuxPalindromo == SAuxBase):
    print("São palíndromos")