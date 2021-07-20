# Faça um programa que peça o tamanho de um arquivo para download (em MB) e
#  a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#  aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Informe o tamanho do arquivo (MB): "))
velocidade_internet = float(input("Informe a velocidade da internet (Mbps): "))
tempo_download = (tamanho_arquivo/velocidade_internet) * 60
print(f"Tempo aproximado do download é {round(tempo_download, 2)} minutos")