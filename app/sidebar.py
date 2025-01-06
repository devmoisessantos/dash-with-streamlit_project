import streamlit as st


def show_sidebar(data):
    st.sidebar.image(
        "assets/logo.png",
        use_column_width=True,
        caption="devmoisessantos"
    )
    st.sidebar.header('Filtros')

    select_region = st.sidebar.multiselect(
        'Selecione a Região',
        data['Regiao'].unique(),
        data['Regiao'].unique()
    )
    filtered_data = data[data['Regiao'].isin(select_region)]
    return filtered_data
