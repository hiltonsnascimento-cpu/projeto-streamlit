import streamlit as st
from banco import criar_tabela, inserir_venda, lista_vendas,excluir_venda

st.set_page_config(
    page_title="Sistema de Cadastro de Vendas",
    layout="wide"
)
st.title("Sistema de Cadastro de Vendas")
criar_tabela()
st.subheader("Cadastrar novas Vendas")