def retornarIntervalo(intervalo=""):
    intervalos = intervalo.split(",")
    resultado = []
    
    for item in intervalos:
        if "-" in item:
            aux = item.split("-")
            inicio_intervalo = int(aux[0])
            fim_intervalo = int(aux[1])
            for numero in range(inicio_intervalo, fim_intervalo + 1):
                resultado.append(numero)
        else:
            resultado.append(int(item))
    
    return resultado


string = "1-3,5,6-10, 12, 64-72"
print(retornarIntervalo(string))

string = "1-3,5,7-9"

print(retornarIntervalo(string))