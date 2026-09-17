import requests
from datetime import datetime
import os

def buscar_cotacoes():
    moedas = "USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{moedas}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao buscar as cotações.")
        return None

def mostrar_cotacoes(dados):
    print("\n=== Cotações Atuais ===\n")
    print(f"Dólar (USD):   R$ {float(dados['USDBRL']['bid']):.2f}")
    print(f"Euro (EUR):    R$ {float(dados['EURBRL']['bid']):.2f}")
    print(f"Libra (GBP):   R$ {float(dados['GBPBRL']['bid']):.2f}")
    print(f"Bitcoin (BTC): R$ {float(dados['BTCBRL']['bid']):,.2f}")

def salvar_historico(dados):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    linha = (
        f"{agora} | "
        f"USD: {float(dados['USDBRL']['bid']):.2f} | "
        f"EUR: {float(dados['EURBRL']['bid']):.2f} | "
        f"GBP: {float(dados['GBPBRL']['bid']):.2f} | "
        f"BTC: {float(dados['BTCBRL']['bid']):.2f}\n"
    )

    with open("historico.txt", "a", encoding="utf=8") as arquivo:
        arquivo.write(linha)

    print("\n✅ Cotações salvas no arquivo historico.txt")

def verificar_alerta(dados):
    print("\n--- Alerta de Preço ---")
    print("1 - Dólar")
    print("2 - Bitcoin")
    print("3 - Euro")
    print("4 - Libra")

    opcao = input("Escolha (1 a 4): ").strip()

    moedas = {
        "1": ("USDBRL", "Dólar"),
        "2": ("BTCBRL", "Bitcoin"),
        "3": ("EURBRL", "Euro"),
        "4": ("GBPBRL", "Libra")
    }

    if opcao not in moedas:
        print("Opção inválida.")
        return
    
    chave, nome = moedas[opcao]
    preco_atual = float(dados[chave]["bid"])
        
    try:
        preco_alvo = float(input(f"Qual o preço máximo que você quer pagar no {nome}? R$ "))
    except ValueError:
        print("Valor Inválido!")
        return

    print(f"\nPreço atual do {nome}: R$ {preco_atual:,.2f}")
    print(f"Seu preço alvo: R$ {preco_alvo:,.2f}")

    if preco_atual <= preco_alvo:
        print(f"\n✅ BOA NOTÍCIA! O {nome} está no seu preço alvo ou mais barato!")
    else:
        diferenca = preco_atual - preco_alvo
        print(f"\n❌ Ainda está caro. Falta baixar R$ {diferenca:,.2f}")

def ver_historico():
    if not os.path.exists("historico.txt"):
        print("\nNenhum histórico encontrado ainda.")
        return

    print("\n=== Historico de Cotações ===\n")
    with open("historico.txt", "r", encoding="utf-8")as arquivo:
        print(arquivo.read())

def menu():
    while True:
        print("\n" + "="*40)
        print("       ROBÔ DE COTAÇÕES")
        print("="*40)
        print("1 - Ver cotações atuais")
        print("2 - Verificar alerta de preço")
        print("3 - Ver histórico")
        print("4 - Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = buscar_cotacoes()
            if dados:
                mostrar_cotacoes(dados)
                salvar_historico(dados)

        elif opcao == "2":
            dados = buscar_cotacoes()
            if dados:
                verificar_alerta(dados)

        elif opcao == "3":
            ver_historico()

        elif opcao == "4":
            print("\nAté mais!👋")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# --- Início do programa ---
menu()