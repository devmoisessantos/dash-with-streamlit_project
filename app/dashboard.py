import streamlit as st
import pandas as pd
from app.kpis import show_kpis
from app.sidebar import show_sidebar
from app.grafic import (grafico_receita_por_regiao, grafico_pedidos_por_tempo,
                        grafico_ticket_medio_por_regiao, grafico_distribuicao_pedidos, grafico_comparacao_regioes)
from app.vendedores import vendedores_tab
from app.handler import load_data


# Configuração inicial do layout
st.set_page_config(page_title="Dashboard", layout="wide")

# Configurando o modo como são tratados os valores floats
pd.options.display.float_format = '{:,.2f}'.format
st.set_option('deprecation.showPyplotGlobalUse', False)


# Carregando os Dados no DataFrame
df = load_data('data/pedidos.csv').copy()

if df is None:
    st.error("Arquivo de dados não encontrado. Por favor, verifique o caminho.")
    st.stop()  # Para a execução do app caso o arquivo não seja encontrado.


def main():
    # Título da Aplicação
    st.title('Dashboard de Vendas :shopping_trolley:')

    # Tabs
    tab1, tab2, tab3 = st.tabs(['Dados e Métricas', 'Gráficos', 'Vendedores'])

    with tab1:
        st.header('Visualização dos Dados')
        st.markdown(
            'Na tabela abaixo, você pode visualizar os dados dos pedidos.')

        # Filtros da Sidebar
        filtered_data = show_sidebar(df)

        # Exibindo o DataFrame filtrado
        st.dataframe(filtered_data)  # Exibe a tabela filtrada com os dados

        # Exibindo os KPIs
        show_kpis(filtered_data)

    with tab2:

        # Título da Aplicação
        st.markdown("""
        ## Análise de Pedidos e Receita
        Abaixo estão os gráficos que ilustram a performance dos pedidos em diferentes regiões, a receita total, 
        o ticket médio, e a distribuição dos pedidos. 
        
        Esses gráficos oferecem uma visão abrangente sobre como os pedidos 
        estão se comportando ao longo do tempo e quais regiões estão gerando mais receita.
        """)
        st.markdown("""
        - **Gráfico 1:** Receita Total por Região — Mostra quanto cada região está contribuindo para a receita total.
        """)
        grafico_receita_por_regiao(df)
        st.markdown("""
        - **Gráfico 2:** Pedidos ao Longo do Tempo — Exibe como os pedidos evoluíram ao longo do tempo, ajudando a identificar tendências.
        """)
        grafico_pedidos_por_tempo(df)
        st.markdown("""
        - **Gráfico 3:** Ticket Médio por Região — Comparação do valor médio dos pedidos entre as regiões.
        """)
        grafico_ticket_medio_por_regiao(df)
        st.markdown("""
        - **Gráfico 4:** Distribuição dos Pedidos por Receita — Exibe a distribuição dos valores dos pedidos.
        """)
        grafico_distribuicao_pedidos(df)
        st.markdown("""
        - **Gráfico 5:** Comparação de Receita Total e Pedidos por Região — Compara o número de pedidos e a receita gerada por cada região.
        """)
        grafico_comparacao_regioes(df)

    with tab3:

        vendedores_tab(df)
