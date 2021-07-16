# Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a-salário bruto.
# b-quanto pagou ao INSS.
# c-quanto pagou ao sindicato.
# d-o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

salario_por_hora = float(input("Qual o valor do salario por hora: "))
horas_trabalhadas = int(input("Número de horas trabalhadas: "))

salario_total = salario_por_hora * horas_trabalhadas
descontos = 0.0

print(f"Total do salario no mê é {salario_total}")

print(f"Salário Bruto {salario_total}")

inss =  (8* salario_total) / 100
print(f"Inss : {inss}")
descontos += inss

ir =  (11* salario_total) / 100
print(f"IR : {ir}")
descontos += ir

sindicato =  (5* salario_total) / 100
print(f"Sindicato : {sindicato}")
descontos += sindicato

print(f"Total de descontos: {descontos}")

salario_liquido = salario_total - descontos
print(f"Salário líquido: {salario_liquido}")


