# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = float(input("Digite o numero real: "))

# o produto do dobro do primeiro com metade do segundo .
resp1 = int(num1 * 2 * num2/2)
print(f"Resposta 1: {resp1}")

# a soma do triplo do primeiro com o terceiro.
resp2 = (num1 * 3) + num3
print(f"Resposta 2: {resp2}")

# o terceiro elevado ao cubo.
resp3 = num3 ** 3
print(f"Resposta 3: {resp3}")
