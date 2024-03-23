# Cálculo de uma compra

def calcular_custo():
    codigo_peca = int(input('Código da peça: '))
    qtd_pecas = int(input('Quantidade de peças: '))
    preco = float(input('Valor unitário: R$'))

    return qtd_pecas * preco

def calcular_total():
    total = 0
    for _ in range(2):
        total += calcular_custo()
    return total

def main():
    total_compra = calcular_total()
    print(f'O valor a pagar é de: RS{total_compra:.2f}')

if __name__ == "__main__":
    main()
    


# total = 0
# for i in range(2):

#     codigo_peca = int(input('Código da peça: '))
#     qtd_pecas = int(input('Quantidade de peças: '))
#     preco = float(input('Valor unitário: R$'))

#     peca_total = qtd_pecas * preco
#     total += peca_total

# print(f'O valor a pagar é de: RS{total:.2f}')
