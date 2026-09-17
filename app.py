import streamlit as st
import requests
from datetime import datetime
import os

# Configuração da página
st.set_page_config(
    page_title="Robô de Cotações",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Robô de Cotações")
st.markdown("Acompanhe as cotações em tempo real")

# Função para buscar cotações
def buscar_cotacoes():
    moedas = "USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()
    return None

# Função para salvar histórico
def salvar_historico(dados):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linha = (
        f"{agora} | "
        f"USD: {float(dados['USDBRL']['bid']):.2f} | "
        f"EUR: {float(dados['EURBRL']['bid']):.2f} | "
        f"GBP: {float(dados['GBPBRL']['bid']):.2f} | "
        f"BTC: {float(dados['BTCBRL']['bid']):.2f}\n"
    )
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)

# Buscar dados
dados = buscar_cotacoes()

if dados:
    # Mostrar cotações em cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("🇺🇸 Dólar (USD)", f"R$ {float(dados['USDBRL']['bid']):.2f}")
        st.metric("🇪🇺 Euro (EUR)", f"R$ {float(dados['EURBRL']['bid']):.2f}")
    
    with col2:
        st.metric("🇬🇧 Libra (GBP)", f"R$ {float(dados['GBPBRL']['bid']):.2f}")
        st.metric("₿ Bitcoin (BTC)", f"R$ {float(dados['BTCBRL']['bid']):,.2f}")
    
    # Botão para atualizar e salvar
    if st.button("🔄 Atualizar e Salvar no Histórico"):
        salvar_historico(dados)
        st.success("Cotações salvas no histórico!")
        st.rerun()

    st.divider()

    # Seção de Alerta de Preço
    st.subheader("🔔 Alerta de Preço")
    
    moeda_escolhida = st.selectbox(
        "Escolha a moeda:",
        ["Dólar", "Bitcoin", "Euro", "Libra"]
    )
    
    mapa_moedas = {
        "Dólar": ("USDBRL", "Dólar"),
        "Bitcoin": ("BTCBRL", "Bitcoin"),
        "Euro": ("EURBRL", "Euro"),
        "Libra": ("GBPBRL", "Libra")
    }
    
    chave, nome = mapa_moedas[moeda_escolhida]
    preco_atual = float(dados[chave]["bid"])
    
    preco_alvo = st.number_input(
        f"Preço máximo desejado para o {nome} (R$):",
        min_value=0.0,
        value=0.0,
        step=0.01
    )
    
    if preco_alvo > 0:
        if preco_atual <= preco_alvo:
            st.success(f"✅ BOA NOTÍCIA! O {nome} está no seu preço alvo ou mais barato!")
            st.write(f"Preço atual: **R$ {preco_atual:,.2f}** | Seu alvo: **R$ {preco_alvo:,.2f}**")
        else:
            diferenca = preco_atual - preco_alvo
            st.warning(f"❌ Ainda está caro. Falta baixar **R$ {diferenca:,.2f}**")
            st.write(f"Preço atual: **R$ {preco_atual:,.2f}** | Seu alvo: **R$ {preco_alvo:,.2f}**")

    st.divider()

    # Histórico
    st.subheader("📜 Histórico de Cotações")
    
    if os.path.exists("historico.txt"):
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            historico = arquivo.read()
        st.text_area("Últimas cotações salvas:", historico, height=200)
    else:
        st.info("Nenhum histórico encontrado ainda. Clique em 'Atualizar e Salvar' para começar.")

else:
    st.error("Erro ao buscar as cotações. Tente novamente mais tarde.")