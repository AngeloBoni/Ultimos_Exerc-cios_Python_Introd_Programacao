import time

nome = input("Digite seu nome: ").upper()
aux = ""

for letra in nome:
    aux = aux + letra
    print(aux)
    time.sleep(0.5)