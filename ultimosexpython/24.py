def definirAprovacao(n1):
    if n1 >= 6:
        return "Aprovado"
    elif n1 >= 4:
        return "Verificação suplementar"
    else:
        return "Reprovado"

n1 = int((input("Digte sua nota média: ")))

situacao = definirAprovacao(n1)

print("Sua situação é: " + situacao)