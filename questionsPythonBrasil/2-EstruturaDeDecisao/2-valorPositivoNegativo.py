# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Informe um valor: "))

if num < 0:
    print(f"{num} é negativo")
else:
    print(f"{num} é positivo")