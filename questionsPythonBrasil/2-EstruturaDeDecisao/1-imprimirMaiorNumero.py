# Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 == num2:
    print(f"{num1} é igual ao {num2}")
else:
    print(f"{num2} é maior que {num1}")
