# Maior entre 3 números
# Fórmula dada: (a + b + abs(a-b)) / 2

def maior_entre_dois(a, b):
    return (a + b + abs(a-b)) / 2

def maior_entre_tres(a, b, c):
    maior_de_ab = maior_entre_dois(a, b)
    maior_de_abc = maior_entre_dois(maior_de_ab, c)
    return maior_de_abc

def main():
    a = int(input('1º valor: '))
    b = int(input('2º valor: '))
    c = int(input('3º valor: '))

    maior = maior_entre_tres(a, b, c)

    print(f'O maior valor entre {a}, {b} e {c} é {maior:.0f}')

if __name__ == '__main__':
    main()