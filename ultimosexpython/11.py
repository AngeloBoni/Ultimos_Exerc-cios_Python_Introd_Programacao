Frase1 = input("Digite a primeira String: ")
Frase2 = input("Digite a segunda String: ")

print(f"String 01: {Frase1}")
print(f"String 02: {Frase2}")

print(f"Tamanho de {Frase1}: {len(Frase1)}")
print(f"Tamanho de {Frase2}: {len(Frase2)}")

if(len(Frase1) == len(Frase2)):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if(Frase1 == Frase2):
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")