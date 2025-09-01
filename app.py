import streamlit as st

st.set_page_config(
    page_title="Corinthians🦅🦅🦅",
    page_icon= "",
    layout= "wide"
)

st.title("Corinthians🦅🦅🦅")
st.subheader("blablablabla")

st.sidebar.header("filtros")
st.sidebar.checkbox("ativar tema escuro", key = "tema")
st.sidebar.slider("selecionar valor", 0, 100, 25)

st.metric("vendas", "R$ 50.000", "+5%")
st.metric("usuários", "R$ 100.000", "-2%")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("coluna 1")
    st.success("tudo certo")
    st.button("clique aqui")

with col2:
    st.header("coluna 2")
    st.success("atenção")
    st.radio("escolha uma opção", ["opção a,", "opção b", "opção c"])

with col3:
    st.header("coluna 3")
    st.info("informação útil")
    st.selectbox("escolha um item", ["item, 1", "item 2", "item 3"])

with st.expander("clique para mais detalhes"):
    st.write("aqui você pode colocar informações adiocionais, gráficos ou tabelas")
    st.checkbox("ativar detalhe")
    st.text_input("digite algo ")
    
st.markdown(
    """
    <div style='background-color:#f9f9f9; padding: 10px; border-radius: 10px'
    <h4 style='color: #FF5733;'>Texto colorido com estilo personalizado</h4>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")
st.markdown("exemplo de bla bla bla")