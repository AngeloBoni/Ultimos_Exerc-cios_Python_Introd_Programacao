telefone = input("Telefone: ")
telefoneaux = ""


for numero in telefone:
    if (numero != "-"):
        telefoneaux += numero

if(len(telefoneaux) == 7):
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
    telefoneaux = "3" + telefoneaux
    telefone = "3" + telefone
    
print(f"Telefone corrigido sem formatação: {telefoneaux}\nTelefone corrigido com formatação: {telefone}")