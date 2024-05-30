# Distância entre 2 pontos
# Fórmula dada: sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

from math import sqrt

def calculo_dist(x1, x2, y1, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    x1 = float(input("Eixo 1: "))
    x2 = float(input("Eixo 2: "))
    y1 = float(input("Eixo 3: "))
    y2 = float(input("Eixo 4: "))

    distancia = calculo_dist(x1, y1, x2, y2)

    print(f"A distância entre os eixos {x1}, {y1}, {x2} e {y2} é de: {distancia:.3f}")

if __name__ == "__main__":
    main()