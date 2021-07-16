# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

tamanho_lado = float(input("Informe a medida do lado do quadrado: "))
area = tamanho_lado**2

print(f"A área do quadrado é {round(area, 2)}")

dobro_area = round(area, 2)**2

print(f"o dobro da área do quadrado é {round(dobro_area, 2)}")