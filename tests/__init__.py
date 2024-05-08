import requests
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$orderby=Data%20desc&$format=json"

requisicao = requests.get(link)
informacoes = requisicao.json()

#exibir dados
tabela = pd.DataFrame(informacoes["value"])
display(tabela)

# pegar todas as informacoes da api
tabela_final = pd.DataFrame()
pular_indice = 0

while True:
    link = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular_indice}&$orderby=Data%20desc&$format=json'
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    tabela = pd.DataFrame(informacoes["value"])
    if len(informacoes['value']) < 1:
        break
    tabela_final = pd.concat([tabela_final, tabela])
    pular_indice += 10000

display(tabela_final)

#Tendência de Uso de Moedas versus Cédulas ao Longo do Tempo
def obter_dados():
    link_base = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$orderby=Data%20desc&$format=json"
    tabela_final = pd.DataFrame()
    pular_indice = 0

    while True:
        link = f'{link_base}&$skip={pular_indice}'
        requisicao = requests.get(link)
        informacoes = requisicao.json()
        tabela = pd.DataFrame(informacoes["value"])
        if len(informacoes['value']) < 1:
            break
        tabela_final = pd.concat([tabela_final, tabela])
        pular_indice += 10000

    return tabela_final

def tendencia_uso_moedas_cedulas(df):
    df['Data'] = pd.to_datetime(df['Data'])  
    df['Ano'] = df['Data'].dt.year 
    df_agrupado = df.groupby(['Ano', 'Especie']).agg({'Quantidade': 'sum'}).reset_index()
    pivot = df_agrupado.pivot(index='Ano', columns='Especie', values='Quantidade').fillna(0)
    pivot['Total'] = pivot['Cédulas'] + pivot['Moedas']
    pivot['% Moedas'] = pivot['Moedas'] / pivot['Total'] * 100
    pivot['% Cédulas'] = pivot['Cédulas'] / pivot['Total'] * 100

    return pivot

dados = obter_dados()
insight_tendencia = tendencia_uso_moedas_cedulas(dados)
print(insight_tendencia)

#Distribuição de Cédulas e Moedas por Denominação
def distribuicao_por_denominacao(df):
    df_agrupado = df.groupby(['Denominacao', 'Especie']).agg({'Quantidade': 'sum'}).reset_index()
    pivot = df_agrupado.pivot(index='Denominacao', columns='Especie', values='Quantidade').fillna(0)

    return pivot

insight_distribuicao_denominacao = distribuicao_por_denominacao(dados)
print(insight_distribuicao_denominacao)

#Flutuações de Quantidade de Cédulas e Moedas por Espécie ao Longo do Tempo
def flutuacoes_quantidade_por_especie(df):
    df['Data'] = pd.to_datetime(df['Data'])
    df_agrupado = df.groupby(['Data', 'Especie']).agg({'Quantidade': 'sum'}).reset_index()
    pivot = df_agrupado.pivot(index='Data', columns='Especie', values='Quantidade').fillna(0)

    return pivot

insight_flutuacoes_quantidade = flutuacoes_quantidade_por_especie(dados)
print(insight_flutuacoes_quantidade)

#Plotando gráfico
anos = insight_tendencia.index
percentual_moedas = insight_tendencia['% Moedas']
percentual_cedulas = insight_tendencia['% Cédulas']

plt.figure(figsize=(10, 6))
plt.plot(anos, percentual_moedas, label='% Moedas')
plt.plot(anos, percentual_cedulas, label='% Cédulas')
plt.xlabel('Ano')
plt.ylabel('Percentual (%)')
plt.title('Tendência de Uso de Moedas versus Cédulas ao Longo do Tempo')
plt.legend()
plt.grid(True)
plt.show()