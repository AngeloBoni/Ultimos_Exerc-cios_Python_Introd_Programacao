import time

def exibirMenu(estado):
    retorno = int(input(f"Estado da memória: {estado}\n"
      "Opções:\n"
      "(1) Somar\n"
      "(2) Subtrair\n"
      "(3) Multiplicar\n"
      "(4) Dividir\n"
      "(5) Limpar memória\n"
      "(6) Sair do programa\n"
      "Qual opção você deseja?: "))
    if retorno == 1:
        return 1
    elif retorno == 2:
        return 2
    elif retorno == 3:
        return 3
    elif retorno == 4:
        return 4
    elif retorno == 5:
        return 5
    elif retorno == 6:
        return -1

def soma():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1 + valor2

def subtracao():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1 - valor2

def multiplicacao():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1 * valor2

def divisao():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    return valor1 / valor2

def printar(resultado):
    time.sleep(1)
    print(f"O resultado a operação é: {resultado}\n")
    time.sleep(1)

estado = 0
escolha = 0

while escolha != -1:
    escolha = exibirMenu(estado)

    if escolha == 1:
        resultado = soma() 
        printar(resultado)
        estado += 1
       

    elif escolha == 2:
        resultado = subtracao()
        printar(resultado)
        estado += 2

    elif escolha == 3:
        resultado = multiplicacao()
        printar(resultado)
        estado += 3

    elif escolha == 4:
        resultado = divisao()
        printar(resultado)
        estado += 4

    elif escolha == 5:
        estado = 0
        time.sleep(1)
    
