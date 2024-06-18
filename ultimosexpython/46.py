def verificarString(string01, string02):
    
    novastring = ""
    

    if(len(string01) > len(string02)):
        j = len(string02)
        for i in range(len(string01)):
            novastring += string01[i]
            if j > 0:
                novastring += string02[i]
                j -= 1
    else:
        j = len(string01)
        for i in range(len(string02)):
            novastring += string02[i]
            if j > 0:
                novastring += string01[i]
                j -= 1

    return novastring

palavara = "Não consigo mais pensar"
palavra1 = "Minha mente esta lenta, 50 exercícios é de foder"

print(verificarString(palavara, palavra1))