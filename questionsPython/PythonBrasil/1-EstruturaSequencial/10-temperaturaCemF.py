# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp = float(input("Informe a temperatura em Celsius: "))
c = ((temp * 9)/5) + 32

print(f"A temperatura em Fahrenheit é {round(c, 1)}")