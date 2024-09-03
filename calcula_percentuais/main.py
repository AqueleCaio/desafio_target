def calcular_percentuais(faturamento):
    # Calcular o valor total de faturamento
    total_faturamento = sum(faturamento.values())

    # Calcular o percentual de representação de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

    return percentuais

def main():
    # Valores de faturamento por estado
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    # Calcular os percentuais
    percentuais = calcular_percentuais(faturamento)

    # Imprimir os resultados
    print(f"Percentual de representação de cada estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
