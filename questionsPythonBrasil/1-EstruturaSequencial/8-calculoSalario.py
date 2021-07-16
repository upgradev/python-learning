# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_por_hora = float(input("Qual o valor do salario por hora: "))
horas_trabalhadas = int(input("Número de horas trabalhadas: "))

salario_total = salario_por_hora * horas_trabalhadas

print(f"Total do salario no mê é {salario_total}")