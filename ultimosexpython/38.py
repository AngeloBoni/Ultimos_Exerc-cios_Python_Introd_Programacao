import math

def calcularDistancia(x1, x2, y1, y2):

    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    d = math.sqrt(d)

    return d

PX = float(input("Digite a localização do primeiro ponto no eixo x: "))
PY = float(input("Digite a localização do primeiro ponto no eixo y: "))

QX = float(input("Digite a localização do segundo ponto no eixo x: "))
QY = float(input("Digite a localização do segundo ponto no eixo y: "))

distancia = calcularDistancia(PX, QX, PY, QY)

distancia = round(distancia, 2)

print(f"A distância dos pontos ({PX}, {PY}) e ({QX}, {QY}) é: {distancia}")