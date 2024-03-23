# Cálculo de salário com bônus e imprimir info do funcionário
def funcionario(nome, salario, total_vendas):
    return nome, salario, total_vendas

def calcular_bonus(salario, total_vendas):
    bonus = (total_vendas * 0.15)
    salario_com_bonus = salario + bonus
    return salario_com_bonus, bonus

def main():
    nome = input('Nome do funcionário: ')
    salario = float(input('Salário sem bônus: '))
    total_vendas = float(input('Vendas realizadas [valor]: R$'))

    salario_com_bonus, bonus = calcular_bonus(salario, total_vendas)

    print(f'O funcionário {nome} receberá R${salario_com_bonus:.2f} de salário com o bônus de {bonus:.2f} das suas vendas')

if __name__ == '__main__':
    main()


