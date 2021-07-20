# João Papo-de-Pescador, homem de bem,
# comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_permitido = 50
peso_pescado = float(input("Qual o peso do peixe? "))
peso_excedido = 0
multa = 0
if peso_pescado > peso_permitido:
    peso_excedido = peso_pescado - peso_permitido
    multa = peso_excedido * 4

print(f"Peso peixe: {peso_pescado}")
print(f"Peso excedido: {round(peso_excedido, 2)}")
print(f"multa: {round(multa, 2)}")