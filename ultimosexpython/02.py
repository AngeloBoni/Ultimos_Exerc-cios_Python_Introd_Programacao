Original = input("Digite a cadeia original do DNA: ")
Original = Original.upper()
Complementar = ""



cont = len(Original)

while cont != 0:
    for elemento in Original:
        if elemento == "A":
            Complementar += "T"
        elif elemento == "T":
            Complementar += "A"
        elif elemento == "C":
            Complementar += "G"
        elif elemento == "G":
            Complementar += "C"
        else:
            Original = input("Foi adicionado um elemento incorreto, repita toda a cadeia: ")
            Original = Original.upper()
            cont = len(Original)
            Complementar = ""
            break;
        cont -= 1

print(f"Nova cadeia: {Complementar}")