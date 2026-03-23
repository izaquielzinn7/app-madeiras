import streamlit as st

# Produtos (todos por metro)
produtos = {
    "CAIBRO": 6.50,
    "RIPA": 3.00,
    "LINHA": 30.00,
    "PRANCHÃO": 43.00,
    "BARROTE": 20.00
}

st.title("🪵 Orçamento de Madeiras")

st.write("Digite a metragem desejada:")

quantidades = {}
total_geral = 0

# Entrada de dados
for nome, preco in produtos.items():
    qtd = st.number_input(
        f"{nome} (R$ {preco:.2f} / metro)",
        min_value=0.0,
        step=0.5,
        format="%.2f"
    )
    
    quantidades[nome] = qtd

# Cálculo automático
st.markdown("Resumo")

for nome, qtd in quantidades.items():
    if qtd > 0:
        preco = produtos[nome]
        subtotal = preco * qtd
        total_geral += subtotal

        st.write(f"{nome} - {qtd:.2f} m x R$ {preco:.2f} = R$ {subtotal:.2f}")

st.write("---")

st.success(f"💰 TOTAL GERAL: R$ {total_geral:.2f}")