# Faça um programa para uma loja de tintas. O programa deverá pedir o
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da
# tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input("Qual o tamanho da área em metros quadrados: "))
valor_lata = 80.0
qtde_latas = 1
qtde_litros_pelo_tamanho = tamanho / 3

if qtde_litros_pelo_tamanho <= 18:
    print(f"Quantidade de lata é {qtde_latas} e o valor é {valor_lata}")
else:
    qtde_latas = qtde_litros_pelo_tamanho / 18
    valor_lata = qtde_latas * valor_lata
    print(
        f"Quantidade de lata é {round(qtde_latas, 2)} e o valor é {round(valor_lata, 2)}")
