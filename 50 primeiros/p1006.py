# Média de 3 notas de um aluno
# A tem peso 2, B tem peso 3 e C tem peso 5

a = float(input('1ª nota: '))
b = float(input('2ª nota: '))
c = float(input('3ª nota: '))

media = ((a * 2) + (b * 3) + (c * 5)) / 10
# dividido por 10 para normalizar a média
# e especificamente 10 pq é a soma dos pesos das 3 notas

print(f'A média do aluno é de: {media:.1f}')
