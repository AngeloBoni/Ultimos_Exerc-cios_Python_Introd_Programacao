def verificarBissexto(ano):
    if (ano % 4 == 0) and (ano % 100 != 0):
        return True
    elif ano % 400 == 0:
        return True

    return False


ano = int(input("Digite o ano: "))

situacao = verificarBissexto(ano)

print("O ano é bissexto? \n" + str(situacao))