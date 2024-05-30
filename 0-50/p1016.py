# Distância entre 2 pontos
# tive dificuldade com os cálculos nessa


def calcular_diferenca_velocidade(velocidade_carro_x, velocidade_carro_y):
    return velocidade_carro_y - velocidade_carro_x

def calcular_distancia_por_minuto(diferenca_velocidade):
    return diferenca_velocidade / 60

def calcular_tempo_necessario(distancia_por_minuto, distancia_alvo):
    return distancia_alvo / distancia_por_minuto

def main():
    velocidade_carro_x = 60
    velocidade_carro_y = 90

    diferenca_velocidade = calcular_diferenca_velocidade(velocidade_carro_x, velocidade_carro_y)
    distancia_por_minuto = calcular_distancia_por_minuto(diferenca_velocidade)

    distancia_alvo = int(input("Distância que o carro Y precisa alcançar em relação ao carro X: "))

    tempo_necessario = calcular_tempo_necessario(distancia_por_minuto, distancia_alvo)

    print(f"Tempo necessário: {tempo_necessario:.0f} minutos para {distancia_alvo} km")

if __name__ == "__main__":
    main()
