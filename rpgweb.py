import streamlit as st

st.set_page_config(page_title="Calculadora de Status RPG", page_icon="🎲")
st.title("🧮 Calculadora de Status RPG")
    
st.sidebar.header("Atributos do Personagem")
agilidade = st.sidebar.number_input("Agilidade", min_value=0, max_value=99, value=0)
vigor = st.sidebar.number_input("Vigor", min_value=0, max_value=99, value=0)
presenca = st.sidebar.number_input("Presença", min_value=0, max_value=99, value=0)
forca = st.sidebar.number_input("Força", min_value=0, max_value=99, value=0)
intelecto = st.sidebar.number_input("Intelecto", min_value=0, max_value=99, value=0)

classe = st.radio(
    "Escolha a sua classe:",
    options=["Combatente", "Especialista", "Ocultista"],
    index=0
).lower()
nex = st.number_input(
    'Quanto de NEX seu personagem possui?:',
    min_value = 0,
    step=5,
    value=0
)
if nex% 5 != 0:
    st.error('5, 10, 15, 20, 25... Entendeu?')
    st.stop()
CLASSES = {
    "combatente": {"vdinicial": 20, "vidaporbloco": 4, "peinicial": 2, "peporbloco": 2, "sanidadeinicial": 12, "sanidadeporbloco": 3},
    "especialista": {"vdinicial": 16, "vidaporbloco": 3, "peinicial": 3, "peporbloco": 3, "sanidadeinicial": 16, "sanidadeporbloco": 4},
    "ocultista": {"vdinicial": 12, "vidaporbloco": 2, "peinicial": 4, "peporbloco": 4, "sanidadeinicial": 20, "sanidadeporbloco": 5}
}

dadosclasses = CLASSES[classe]
nexinicial = 5
totalnex = nex
nexsubido = nex - nexinicial
nexadd = nexsubido // 5

totalpe = (dadosclasses["peinicial"] + presenca) + (dadosclasses["peporbloco"] + presenca) * nexadd
totalvd = (dadosclasses["vdinicial"] + vigor) + (dadosclasses["vidaporbloco"] + vigor) * nexadd
totalsan = (dadosclasses["sanidadeinicial"]) + (dadosclasses["sanidadeporbloco"]) * nexadd
defesa = 10 + agilidade

st.subheader('=== Status Final ===')

col1, col2 = st.columns(2)

with col1:
    st.metric("NEX:", f"{totalnex}%")
    st.metric("Pontos de Vida (PV):", totalvd)
with col2:
    st.metric("Pontos de Esforço (PE):", totalpe)
    st.metric("Sanidade:", totalsan)
st.metric("Defesa:", f"{defesa}" + " + Modificadores (armaduras e habilidades)")
