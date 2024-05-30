# Para descobrir o volume de uma esfera
# Fórmula dada: (4/3) * pi * R3

import math

raio = float(input('Valor do raio: '))

def calcular_volume(valor_raio):
    return (4.0/3) * math.pi * valor_raio ** 3

def main():
    raio_volume = calcular_volume(raio)

    print(f'O volume de uma esfera com {raio} de raio é de {raio_volume:.3f}')

if __name__ == '__main__':
    main()