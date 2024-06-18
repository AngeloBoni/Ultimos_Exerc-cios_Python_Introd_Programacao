nome = input("Digite seu nome: ")
nome_alternativo = ''

for i in range(len(nome) - 1, -1, -1):
    nome_alternativo += nome[i]

nome = nome_alternativo.upper()

print("Seu nome ao contrário é: " + nome)

