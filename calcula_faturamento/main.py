import json
import numpy as np
import os

def calcular_faturamento(dados):
    faturamentos = np.array([dia["valor"] for dia in dados])
    faturamentos_validos = faturamentos[faturamentos > 0]

    menor_faturamento = np.min(faturamentos_validos)
    maior_faturamento = np.max(faturamentos_validos)
    media_faturamento = np.mean(faturamentos_validos)
    dias_acima_media = np.sum(faturamentos_validos > media_faturamento)

    print()
    print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    print()
# Verifica se o arquivo existe
file_path = 'dados.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        dados = json.load(file)
    calcular_faturamento(dados)
else:
    print(f"Erro: Arquivo '{file_path}' não encontrado. Verifique o caminho e o nome do arquivo.")
