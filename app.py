import streamlit as st
import pandas as pd

st.set_page_config(page_title="Orçamento de Materiais", layout="wide")

# 1. INICIALIZAÇÃO DOS DADOS
if 'lista_precos' not in st.session_state:
    st.session_state.lista_precos = [
        {"Material": "CAIBRO", "Preço": 6.50},
        {"Material": "RIPA", "Preço": 3.00},
        {"Material": "LINHA", "Preço": 30.00},
        {"Material": "BARROTE", "Preço": 20.00},
        {"Material": "PRANCHÃO", "Preço": 8700.00},
    ]

if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# ID para resetar APENAS os campos numéricos
if 'input_reset_id' not in st.session_state:
    st.session_state.input_reset_id = 0

st.title("Orçamento de Materiais - Modo Balcão")

# --- BARRA LATERAL: CONFIGURAÇÕES ---
with st.sidebar:
    st.header("Configurações")
    st.session_state.lista_precos = st.data_editor(
        st.session_state.lista_precos, 
        num_rows="dynamic", 
        key="config_precos"
    )
    
    if st.button("Limpar Orçamento Inteiro"):
        st.session_state.carrinho = []
        st.rerun()

# Busca de preços
dict_precos = {item.get("Material", "").upper(): item.get("Preço", 0.0) for item in st.session_state.lista_precos if item.get("Material")}

# --- ÁREA DE LANÇAMENTO ---
with st.container(border=True):
    st.subheader("Adicionar Item")
    
    c1, c2, c3 = st.columns([2, 1, 1])
    
    with c1:
        material_sel = st.selectbox(
            "Material", 
            options=list(dict_precos.keys()),
            key="material_fixo" 
        )
    with c2:
        # A chave muda a cada adição, então o valor VOLTA PARA 1
        qtd_sel = st.number_input(
            "Quantidade", min_value=1, step=1, 
            key=f"qtd_{st.session_state.input_reset_id}"
        )
    with c3:
        # A chave muda a cada adição, então o valor VOLTA PARA 0.0
        met_sel = st.number_input(
            "Comprimento (m)", min_value=0.0, step=0.5, format="%.2f",
            key=f"met_{st.session_state.input_reset_id}"
        )

    subtotal = 0
    detalhe_medida = f"{met_sel:.2f}m"
    
    # PRANCHÃO
    if material_sel == "PRANCHÃO":
        st.markdown("---")
        st.info("Medidas do Pranchão")
        cx1, cx2 = st.columns(2)
        with cx1:
            larg_cm = st.number_input("Largura (cm)", min_value=1.0, step=1.0, key=f"larg_{st.session_state.input_reset_id}")
        with cx2:
            alt_cm = st.number_input("Altura (cm)", min_value=1.0, step=1.0, key=f"alt_{st.session_state.input_reset_id}")
        
        p_unit_m3 = dict_precos.get(material_sel, 0.0)
        volume = met_sel * (larg_cm/100) * (alt_cm/100)
        subtotal = (qtd_sel * volume) * p_unit_m3
        detalhe_medida = f"{met_sel:.2f}m x {larg_cm}cm x {alt_cm}cm"
    else:
        p_unit = dict_precos.get(material_sel, 0.0)
        subtotal = (qtd_sel * met_sel) * p_unit

    if st.button("Adicionar ao Pedido", use_container_width=True):
        if material_sel and met_sel > 0:
            st.session_state.carrinho.append({
                "Material": material_sel,
                "Qtd": qtd_sel,
                "Medidas": detalhe_medida,
                "Subtotal": subtotal
            })
            st.session_state.input_reset_id += 1
            st.rerun()
        else:
            st.warning("Informe uma metragem válida antes de adicionar.")

# --- RESUMO ---
st.subheader("Itens no Orçamento")

if st.session_state.carrinho:
    df = pd.DataFrame(st.session_state.carrinho)
    df_excluir = df.copy()
    df_excluir["Subtotal"] = df_excluir["Subtotal"].map("R$ {:.2f}".format)
    st.table(df_excluir)
    
    total_final = sum(item["Subtotal"] for item in st.session_state.carrinho)
    st.metric(label="TOTAL GERAL", value=f"R$ {total_final:.2f}")
    
    if st.button("Remover Último"):
        st.session_state.carrinho.pop()
        st.rerun()
else:
    st.info("Pedido vazio.")
