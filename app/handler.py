import pandas as pd
import streamlit as st


@st.cache
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        st.error("Arquivo de dados não encontrado. Por favor, verifique o caminho.")
        st.stop()
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        st.stop()
