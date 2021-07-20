# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")
if len(letra) > 1:
    print("É uma palavra ou frase")
elif letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print("É vogal")
else:
    print("Consoante")