import time

nome = input("Digite seu nome: ").upper()
aux = ""

print(nome)
time.sleep(0.5)

for i in range(len(nome) - 1, -1, -1):
   
    for j in range(i):
        aux += nome[j]
    
    print(aux)
    aux = ""
    time.sleep(0.5)
 