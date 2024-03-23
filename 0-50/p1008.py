# Cálculo de salário e imprimir info do funcionário

def calculo_salario(horas_trabalhadas, valor_por_hora):
    salario = horas_trabalhadas * valor_por_hora
    return salario

def main():
    numero_do_funcionario = int(input('Número do funcionario: '))
    horas_trabalhadas = int(input('Horas trabalhadas: '))
    valor_por_hora = float(input('Valor por hora: '))
    
    salario = calculo_salario(horas_trabalhadas, valor_por_hora)
    print(f'O funcionário {numero_do_funcionario} trabalha {horas_trabalhadas} horas e recebe um salário de R${salario:.2f}')

if __name__ == "__main__":
    main()