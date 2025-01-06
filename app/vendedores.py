import streamlit as st


def vendedores_tab(data):

    # Resumo de Vendedores
    st.subheader("Resumo de Vendedores")

    # Usando a coluna 'ReceitaTotal' para o agrupamento
    total_vendas_vendedor = data.groupby(
        'Vendedor')['ReceitaTotal'].sum().reset_index()

    # Exibindo o gráfico de barras com a receita total ajustada por vendedor
    st.bar_chart(data=total_vendas_vendedor, x='Vendedor',
                 y='ReceitaTotal', use_container_width=True)

    # Melhor Vendedor
    melhor_vendedor = total_vendas_vendedor.loc[total_vendas_vendedor['ReceitaTotal'].idxmax(
    )]['Vendedor']
    st.metric(label="Melhor Vendedor", value=melhor_vendedor)

    # Filtro por Vendedor
    vendedor_selecionado = st.selectbox(
        "Selecione um Vendedor", data['Vendedor'].unique())
    data_vendedor = data[data['Vendedor'] == vendedor_selecionado]

    # Tabela de Pedidos do Vendedor Selecionado
    st.subheader(f"Detalhamento de Pedidos - {vendedor_selecionado}")
    data_vendedor.loc[:,
                      'ReceitaTotal'] = data_vendedor['ReceitaTotal'].round(2)
    st.dataframe(data_vendedor[['DataPedido', 'Regiao', 'ReceitaTotal']])

    # Gráficos Adicionais
    st.subheader("Receita ao Longo do Tempo por Vendedor")
    receita_por_tempo = data_vendedor.groupby(data_vendedor['DataPedido'])[
        'ReceitaTotal'].sum().reset_index()
    st.line_chart(data=receita_por_tempo, x='DataPedido',
                  y='ReceitaTotal', use_container_width=True)
