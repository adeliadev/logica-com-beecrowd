# Cálculo da área de várias formas geográficas

import math

def area_triangulo_retangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return math.pi * raio ** 2

def area_trapezio(base_menor, base_maior, altura):
    return ((base_menor + base_maior) * altura) / 2

def area_quadrado(lado):
    return lado**2

def area_retangulo(lado1, lado2):
    return lado1 * lado2


def main():
    a = float(input('lado a: '))
    b = float(input('lado b: '))
    c = float(input('lado c: '))

    triangulo = area_triangulo_retangulo(a, c)
    circulo = area_circulo(c)
    trapezio = area_trapezio(a, b, c)
    quadrado = area_quadrado(b)
    retangulo = area_retangulo(a, b)

    formatacao = f'''Triangulo: {triangulo:.3f}
    Círculo: {circulo:.3f}
    Trapézio: {trapezio:.3f}
    Quadrado: {quadrado:.3f}
    Retângulo: {retangulo:.3f}'''

    print(formatacao)
