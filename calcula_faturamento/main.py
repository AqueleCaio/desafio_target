import numpy as np

def calcula_faturamento(faturamento):
    # Remover dias sem faturamento
    faturamento_validos = faturamento[faturamento > 0]

    # Pega o valor minimo dos faturamentos
    min_faturamento = np.min(faturamento_validos)

    # Pega o valor máximo dos faturamentos
    max_faturamento = np.max(faturamento_validos)

    # Pega a média dos faturamentos
    media = np.mean(faturamento_validos)

    # Número de dias com faturamento superior à média mensal
    faturamento_superior = np.sum(faturamento_validos > media)

    # Printando os resultados dentro da função
    print()
    print(f"Faturamentos diário: {faturamento}\n")
  
    print(f"Menor valor de faturamento: {min_faturamento:.2f}")
    print(f"Maior valor de faturamento: {max_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {faturamento_superior}")
    print()

# Gera um array de faturamento diário aleatório
faturamento = np.random.randint(0, 10000, size=30)

calcula_faturamento(faturamento)
