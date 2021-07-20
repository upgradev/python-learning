# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math
raio =  float(input("Informa o raio do círculo: ")) 
area = (raio**2) * math.pi

print(f"A área do raio {raio} é {round(area, 2)}")