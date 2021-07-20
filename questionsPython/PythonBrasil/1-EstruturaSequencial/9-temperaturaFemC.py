# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temp = float(input("Informe a temperatura em Fahrenheit: "))
c = 5 * ((temp- 32)/9)

print(f"A temperatura em Celsius é {round(c, 1)}")