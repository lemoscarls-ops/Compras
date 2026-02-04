import streamlit as st

st.title("🛒 Gestor de Compras")

if 'itens' not in st.session_state:
    st.session_state.itens = [{"nome": "", "preco": 0.0}]

if st.button("+ Adicionar Item"):
    st.session_state.itens.append({"nome": "", "preco": 0.0})

total = 0.0
for i, item in enumerate(st.session_state.itens):
    col1, col2 = st.columns([2, 1])
    with col1:
        item["nome"] = st.text_input(f"O que vais comprar? {i+1}", value=item["nome"], key=f"n{i}")
    with col2:
        item["preco"] = st.number_input(f"Preço (Kz) {i+1}", value=float(item["preco"]), key=f"p{i}")
        total += item["preco"]

st.divider()
pessoas = st.number_input("Dividir por quantas pessoas?", min_value=1, value=8)

if total > 0:
    cada = total / pessoas
    st.success(f"**Total:** {total:,.2f} Kz")
    st.info(f"**Cada um paga:** {cada:,.2f} Kz")
