# 1 litro = 12km
def calculo_litros(velocidade, horas):
    distancia_final = velocidade * horas
    calculo_litros = distancia_final / 12
    return calculo_litros

def main():
    horas = int(input("Horas: "))
    velocidade = int(input("Velocidade média: "))

    calculo_final = calculo_litros(velocidade, horas)

    print(f"Foram necessários {calculo_final:.3f} litros de combustível para uma viagem de {horas} horas ")

if __name__ == "__main__":
    main()