# Média de um aluno com 2 notas
# A tem peso 3.5 e b tem peso 7.5

a = float(input('1ª nota: '))
b = float(input('2ª nota: '))

media = (((a * 3.5) + (b * 7.5)) / 11)
# dividido por 11 para normalizar a media
# e especificamente 11 pq é a soma dos pesos das 2 notas

print(f'A média do aluno é de: {media:.1f}')