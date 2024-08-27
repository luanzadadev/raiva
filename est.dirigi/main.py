#custo de pedido CPA/S
#custo de manutenção H/CA
#lec = (2 * ca * cc) / (cpa *pu)


import math
import locale

def main():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    print("*Lote Econômico de Compras (LEC)*\n")
    print("CA = Consumo Anual em Quantidade.")
    print("CC = Custo do Pedido de Compra.")
    print("CPA = Custo do Material Armazenado.")
    print("PVC = Preço Unitário.\n")

    CA = float(input("Digite o CA: "))
    CC = float(input("Digite o CC: "))
    CPA = float(input("Digite o CPA: "))
    PU = float(input("Digite o PU: "))

    # Calculando o LEC
    LEC = (2 * CA * CC) / (CPA * PU)
    raiz = math.sqrt(LEC)
    qtcompra = CA / raiz

    # Calculando os custos
    CP = (CA * CC) / raiz
    CArmazenagem = (raiz * PU * CPA) / 2
    CT = CP + CArmazenagem

    

    # Exibindo os resultados
    print(f"\nO resultado da divisão é: {LEC:.2f}")
    print(f"O LEC é: {raiz:.2f}")
    print(f"A Quantidade de compra é: {qtcompra:.2f}")
    print(f"O Custo Total é: {CT:.2f}")

if __name__ == "__main__":
    main()
