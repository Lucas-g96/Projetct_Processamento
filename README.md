# Análise de Dinheiro em Circulação

Este projeto visa analisar e visualizar dados sobre dinheiro em circulação, utilizando a API do Banco Central do Brasil para obter informações diárias sobre o tema.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- requests
- matplotlib
- pandas

## Instalação
Para instalar as bibliotecas necessárias, você pode usar o comando:

    pip install requests matplotlib pandas psycopg2 sqlalchemy

No meu caso, estou fazendo o gerenciamento de versão com a biblioteca Poetry, dito isto, tudo que se for instalado usando essa arquitetura segue o padrão:

    Poetry add 'LIB'

## Uso

- 1 - Execute o código para obter os dados da API do Banco Central.

- 2 - Será exibida uma tabela com as informações obtidas.

- 3 - O código também realiza análises e gera insights sobre tendências de uso de moedas versus cédulas, distribuição por denominação e flutuações de quantidade por espécie ao longo do tempo.

- 4 - Por fim, um gráfico é gerado para visualizar a tendência de uso de moedas versus cédulas ao longo do tempo.

## Funcionalidades

## Obter Dados da API
A função obter_dados() faz uma solicitação à API do Banco Central para obter informações diárias sobre dinheiro em circulação.

## Tendência de Uso de Moedas versus Cédulas ao Longo do Tempo
A função tendencia_uso_moedas_cedulas(df) analisa os dados obtidos para mostrar a tendência de uso de moedas versus cédulas ao longo do tempo, calculando o percentual de moedas e cédulas em relação ao total.

## Distribuição de Cédulas e Moedas por Denominação
A função distribuicao_por_denominacao(df) agrupa os dados por denominação e espécie (cédulas ou moedas), mostrando a distribuição quantitativa por cada tipo de dinheiro.

## Flutuações de Quantidade de Cédulas e Moedas por Espécie ao Longo do Tempo
A função flutuacoes_quantidade_por_especie(df) analisa as flutuações na quantidade de cédulas e moedas ao longo do tempo, mostrando como a quantidade varia para cada espécie de dinheiro.

## Exemplo de Uso

    import requests
    import matplotlib.pyplot as plt
    import pandas as pd

    # Executar funções e plotar gráfico
    dados = obter_dados()
    insight_tendencia = tendencia_uso_moedas_cedulas(dados)
    insight_distribuicao_denominacao = distribuicao_por_denominacao(dados)
    insight_flutuacoes_quantidade = flutuacoes_quantidade_por_especie(dados)

    # Plotar gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(anos, percentual_moedas, label='% Moedas')
    plt.plot(anos, percentual_cedulas, label='% Cédulas')
    plt.xlabel('Ano')
    plt.ylabel('Percentual (%)')
    plt.title('Tendência de Uso de Moedas versus Cédulas ao Longo do Tempo')
    plt.legend()
    plt.grid(True)
    plt.show()


![Link]()


## Contribuição
Fique à vontade para contribuir com melhorias neste projeto. Basta abrir uma issue ou enviar um pull request com suas sugestões.