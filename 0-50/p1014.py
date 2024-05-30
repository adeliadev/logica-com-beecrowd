# Consumo médio de combustível

def consumo_medio(x, y):
    return x / y

def main():
    x = int(input("Digite os km percorridos: "))
    y = float(input("Total de combustível gasto: "))

    media = consumo_medio(x, y)

    print(f"O consumo médio de combustível para {x}km é de: {media:.3f} litros")

if __name__ == "__main__":
    main()