# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"maior numero {num1}")
    if num2 > num3:
        print(f"menor número: {num3}")
    else:
        print(f"menor número: {num2}")
elif num2 > num1 and num2 > num3:
    print(f"maior numero {num2}")
    if num1 > num3:
        print(f"menor número: {num3}")
    else:
        print(f"menor número: {num1}")
else:
    print(f"maior numero {num3}")
    if num1 > num2:
        print(f"menor número: {num2}")
    else:
        print(f"menor número: {num1}")
