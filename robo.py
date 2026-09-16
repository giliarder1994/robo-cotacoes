import requests

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

def verificar_alerta(dados):
    print("\n--- Alerta de Preço ---")

    print("Qual moeda você quer monitorar? ")
    print("1 - Dólar")
    print("2 - Bitcoin")
    print("3 - Euro")
    print("4 - Libra")
    opcao = input("Escolha entra as opções: ").strip()

    if opcao == "1":
        preco_atual = float(dados["USDBRL"]["bid"])
        nome = "Dólar"
    elif opcao == "2":
        preco_atual = float(dados["BTCBRL"]["bid"])
        nome = "Bitcoin"
    elif opcao == "3":
        preco_atual = float(dados["EURBRL"]["bid"])
        nome = "Euro"
    elif opcao == "4":
        preco_atual = float(dados["GBPBRL"]["bid"])
        nome = "Libra"
    else:
        print("Opção inválida.")
        return
    
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

# --- Programa principal ---
print("=== Robô de Cotações ===\n")

dados = buscar_cotacoes()

if dados:
    mostrar_cotacoes(dados)
    verificar_alerta(dados)
