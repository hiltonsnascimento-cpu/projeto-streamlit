#app_escola.py
import streamlit as st
import pandas as pd

dados = {
    "curso": [ "Reforço de Matemática","Inglês Básico","Robótica","Teatro","Reforço de Português","Espanhol","Xadrez","Pintura"],

    "categoria": ["Exatas", "Idiomas", "Tecnologia", "Arte", "Humanas", "Idiomas", "Tecnologia", "Arte"],

    "valor": [ 120.0, 150.0, 200.0, 100.0,120.0,140.0, 90.0, 110.0],

    "carga_horaria": [ 4, 3, 5, 2,4,3,  2, 3],

    "avaliacao": [4.7, 4.3, 4.9, 4.5, 4.2, 4.4, 4.6, 4.8]
}
df = pd.DataFrame(dados)


st.title("Escola Nova Geração")
st.write(
    "Acompanhamento dos cursos extracurriculares, "
    "mensalidades, categorias, carga horária e avaliações."
)


st.header("Tabela de Cursos")
st.dataframe( df, use_container_width=True)

quantidade_cursos = len(df)

valor_total = df["valor"].sum()

media_mensalidade = df["valor"].mean()

media_avaliacao = df["avaliacao"].mean()

carga_horaria_media = df["carga_horaria"].mean()


st.header("Indicadores")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total de cursos", quantidade_cursos)

with col2:
    st.metric("Arrecadação mensal", f"R$ {valor_total:,.2f}")

with col3:
    st.metric("Mensalidade média", f"R$ {media_mensalidade:,.2f}")

with col4:
    st.metric("Avaliação média", f"{media_avaliacao:.1f}")

with col5:
    st.metric("Carga horária média", f"{carga_horaria_media:.1f} h")


st.header("Mensalidade por Curso")
grafico_valor = df.set_index("curso")["valor"]
st.bar_chart(grafico_valor)


st.header("Cursos por Categoria")
cursos_categoria = df["categoria"].value_counts()
st.bar_chart(cursos_categoria)


st.header("Avaliação dos Cursos")
avaliacoes = df.set_index("curso")["avaliacao"]
st.bar_chart(avaliacoes)


st.header("Carga Horária por Curso")
carga = df.set_index("curso")["carga_horaria"]
st.bar_chart(carga)