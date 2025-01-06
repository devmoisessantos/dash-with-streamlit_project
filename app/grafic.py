import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


def grafico_receita_por_regiao(data):
    receita_por_regiao = data.groupby(
        'Regiao')['ReceitaTotal'].sum().reset_index()
    st.bar_chart(x='Regiao', y='ReceitaTotal',
                 data=receita_por_regiao, use_container_width=True)


def grafico_pedidos_por_tempo(data):
    # Convertendo 'DataPedido' para datetime
    data['DataPedido'] = pd.to_datetime(data['DataPedido'])

    # Agrupando por dia (ou outro intervalo desejado)
    pedidos_por_dia = data.groupby(
        data['DataPedido'].dt.date).size().reset_index(name='Quantidade')

    # Ajustando o gráfico
    st.line_chart(x='DataPedido', y='Quantidade',
                  data=pedidos_por_dia, use_container_width=True)


def grafico_ticket_medio_por_regiao(data):
    ticket_medio_por_regiao = data.groupby(
        'Regiao')['ReceitaTotal'].sum() / data.groupby('Regiao').size()
    ticket_medio_por_regiao = ticket_medio_por_regiao.reset_index(
        name='Ticket Médio')
    st.bar_chart(x='Ticket Médio', y='Regiao',
                 data=ticket_medio_por_regiao, use_container_width=True)


def grafico_distribuicao_pedidos(data):
    data = data['ReceitaTotal']
    fig, ax = plt.subplots()
    sns.histplot(data, bins=30, kde=True, color='blue',
                 edgecolor='black', ax=ax)
    ax.set_title('Distribuição de Pedidos por Receita')
    ax.set_xlabel('Valor do Pedido (R$)')
    ax.set_ylabel('Quantidade de Pedidos')

    # Exibir o histograma no Streamlit
    st.pyplot(fig)


def grafico_comparacao_regioes(data):
    # Agrupar dados por região
    resumo_regioes = data.groupby('Regiao').agg(
        {'ReceitaTotal': 'sum', 'DataPedido': 'count'}).reset_index()

    # Exibir gráficos lado a lado usando colunas do Streamlit
    col1, col2 = st.columns(2)

    # Gráfico de barras para Receita Total na primeira coluna
    with col1:
        st.bar_chart(resumo_regioes.set_index('Regiao')['ReceitaTotal'])
        st.subheader('Receita Total por Região')

    # Gráfico de linha para Total de Pedidos na segunda coluna
    with col2:
        st.line_chart(resumo_regioes.set_index('Regiao')['DataPedido'])
        st.subheader('Total de Pedidos por Região')
