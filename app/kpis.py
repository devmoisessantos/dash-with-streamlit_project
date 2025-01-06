import numpy as np
import streamlit as st


def show_kpis(data):

    # Opção para escolher se quer ver os KPIs de uma região ou de todos
    opcao = st.sidebar.radio("Selecione uma opção", ("Por Região", "Total"))

    if opcao == "Por Região":
        # Filtro por região na sidebar
        regiao_selecionada = st.sidebar.selectbox(
            "Selecione uma Região", data['Regiao'].unique())

        # Filtrando os dados pela região selecionada
        data_regiao = data[data['Regiao'] == regiao_selecionada]
    else:
        # Se a opção for "Total", considera todos os dados
        data_regiao = data

    # Total de Pedidos
    total_pedidos = data_regiao.shape[0]

    # Receita Total
    receita = data_regiao['ReceitaTotal'].sum()

    receita_total = np.round(receita, 2)

    # Ticket Médio
    ticket_medio = receita_total / total_pedidos if total_pedidos > 0 else 0

    # Pedidos por Dia
    pedidos_por_dia = data_regiao.groupby(
        data_regiao['DataPedido']).size().mean()

    # Layout dos KPIs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total de Pedidos", value=total_pedidos)

    with col2:
        st.metric(label="Receita Total", value=f"R$ {receita_total:,.2f}")

    with col3:
        st.metric(label="Ticket Médio", value=f"R$ {ticket_medio:,.2f}")

    with col4:
        st.metric(label="Pedidos por Dia (Média)",
                  value=f"{pedidos_por_dia:.2f}")
