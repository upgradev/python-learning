# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_digitada = input("Informe a letra F ou M ")
if letra_digitada.upper() == "F":
    print("Feminino")
elif letra_digitada.upper() == "M":
    print("Masculino")
else:
    print("Sexo invalido")