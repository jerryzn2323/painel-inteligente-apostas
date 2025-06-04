
import streamlit as st
from jogos_api import buscar_jogos
from odds_api import buscar_odds
from regras_aposta import gerar_sugestao

st.set_page_config(layout="wide")
st.title("⚽ Painel Inteligente de Apostas Esportivas")

st.sidebar.title("🔍 Filtros")
liga = st.sidebar.selectbox("Liga", ["PL", "PD", "SA", "BL1", "FL1"])
data = st.sidebar.date_input("Data", help="Selecione o dia dos jogos")

st.info("🔄 Carregando dados dos jogos e odds reais...")

jogos = buscar_jogos(liga)
odds = buscar_odds("soccer", region="uk")

if not jogos:
    st.warning("Nenhum jogo encontrado para a liga selecionada.")
else:
    for jogo in jogos:
        st.markdown(f"## ⚽ {jogo['homeTeam']} x {jogo['awayTeam']}")
        st.write(f"Status: {jogo['status']}")
        sug = gerar_sugestao(jogo, odds)
        st.success(f"📌 Sugestão de aposta: **{sug}**")
        st.markdown("---")
