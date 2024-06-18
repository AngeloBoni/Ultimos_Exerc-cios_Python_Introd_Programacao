def calcularGrupos(N, M):

    fatorial_N = 1
    fatorial_M = 1
    fatorial_NM = 1
    NM = N - M

    for i in range(N, 0, -1):
        fatorial_N *= i
    for i in range(M, 0, -1):
        fatorial_M *= i
    for i in range(NM, 0, -1):
        fatorial_NM *= i

    return fatorial_N/(fatorial_M * fatorial_NM)



N = int(input("Digite o total de alunos da turma: "))
M = int(input("Digite quantos alunos no primeiro grupo: "))

possibilidades = calcularGrupos(N, M)

print(f"O número total de possibilidades é: {possibilidades}")