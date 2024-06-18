data = input("Digite a data no modelo dd/mm/aaaa: ")
data = data.split("/")

if(data[1] == "01"):
    data[1] = "janeiro"
elif(data[1] == "02"):
    data[1] = "fevereiro"
elif(data[1] == "03"):
    data[1] = "março"
elif(data[1] == "04"):
    data[1] = "abril"
elif(data[1] == "05"):
    data[1] = "maio"
elif(data[1] == "06"):
    data[1] = "junho"
elif(data[1] == "07"):
    data[1] = "julho"
elif(data[1] == "08"):
    data[1] = "agosto"
elif(data[1] == "09"):
    data[1] = "setembro"
elif(data[1] == "10"):
    data[1] = "outubro"
elif(data[1] == "11"):
    data[1] = "novembro"
elif(data[1] == "12"):
    data[1] = "dezembro"
else:
    print("Mês inválido!")
    data[1] = "!Mês inválido!"

print(f"Você nasceu em {data[0]} de {data[1]} de {data[2]}")