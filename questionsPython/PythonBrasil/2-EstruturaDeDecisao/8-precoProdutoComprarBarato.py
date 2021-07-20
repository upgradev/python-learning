# Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    print(f"Produto com o melhor preço é o produto 1 {prod1}")
elif prod2 < prod1 and prod2 < prod3:
    print(f"Produto com o melhor preço é o produto 2 {prod2}")
else:
    print(f"Produto com o melhor preço é o produto 3 {prod3}")