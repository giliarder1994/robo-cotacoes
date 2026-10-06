# 💰 Robô de Cotações

Aplicação desenvolvida em **Python** para consultar cotações de moedas e Bitcoin em tempo real, armazenar um histórico de valores e permitir a configuração de alertas de preço.

O projeto possui duas versões: uma aplicação executada pelo terminal e uma interface web desenvolvida com **Streamlit**.

## 📌 Sobre o Projeto

O **Robô de Cotações** foi desenvolvido com o objetivo de praticar conceitos de Python através de uma aplicação que consome dados de uma API externa e apresenta informações de forma simples e interativa.

A aplicação consulta cotações em relação ao Real Brasileiro (BRL) para:

* 🇺🇸 Dólar (USD)
* 🇪🇺 Euro (EUR)
* 🇬🇧 Libra (GBP)
* ₿ Bitcoin (BTC)

Além de consultar os valores atuais, o projeto permite salvar um histórico das cotações e verificar se uma determinada moeda atingiu o preço máximo definido pelo usuário.

## 🚀 Funcionalidades

### 📊 Consulta de cotações

A aplicação realiza uma requisição para a API de cotações e obtém os valores atuais de:

* USD/BRL
* EUR/BRL
* GBP/BRL
* BTC/BRL

Os valores são processados e apresentados em Reais (R$).

### 📜 Histórico de cotações

A aplicação permite salvar as cotações consultadas em um arquivo:

```text
historico.txt
```

Cada registro contém:

* Data e hora da consulta
* Cotação do Dólar
* Cotação do Euro
* Cotação da Libra
* Cotação do Bitcoin

Exemplo:

```text
17/09/2026 14:34:20 | USD: 5.15 | EUR: 5.92 | GBP: 6.88 | BTC: 397133.00
```

### 🔔 Alerta de preço

O usuário pode escolher uma moeda e definir um preço máximo que deseja pagar.

A aplicação compara o preço atual com o preço informado e apresenta uma mensagem indicando se o valor atingiu o objetivo.

Exemplo:

```text
Preço atual: R$ 5,15
Preço alvo: R$ 5,20

✅ O Dólar está no seu preço alvo ou mais barato!
```

Caso o preço atual esteja acima do objetivo:

```text
❌ Ainda está caro. Falta baixar R$ 0,15
```

## 🖥️ Interface Web

Além da versão executada pelo terminal, o projeto possui uma interface web desenvolvida com **Streamlit**.

A interface apresenta as cotações utilizando cards:

* Dólar
* Euro
* Libra
* Bitcoin

Também permite:

* 🔄 Atualizar as cotações.
* 💾 Salvar os valores no histórico.
* 🔔 Configurar alertas de preço.
* 📜 Visualizar o histórico de cotações.

## 📂 Estrutura do projeto

```text
robo-cotacoes/
│
├── app.py
├── robo.py
├── historico.txt
└── README.md
```

### `app.py`

Responsável pela versão web da aplicação utilizando Streamlit.

Principais responsabilidades:

* Criar a interface gráfica.
* Consultar a API.
* Exibir as cotações.
* Salvar o histórico.
* Verificar alertas de preço.
* Exibir o histórico salvo.

### `robo.py`

Responsável pela versão executada diretamente no terminal.

Possui um menu interativo com opções para:

```text
1 - Ver cotações atuais
2 - Verificar alerta de preço
3 - Ver histórico
4 - Sair
```

### `historico.txt`

Arquivo utilizado para armazenar as cotações consultadas ao longo do tempo.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Streamlit** — criação da interface web
* **Requests** — consumo da API de cotações
* **Datetime** — registro de data e hora
* **OS** — manipulação e verificação de arquivos
* **AwesomeAPI** — fonte dos dados de cotação

## 🌐 API utilizada

As cotações são obtidas através da **AwesomeAPI**.

Endpoint utilizado:

```text
https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL
```

A aplicação realiza uma requisição HTTP e utiliza os dados retornados em formato JSON.

## ⚙️ Instalação

Certifique-se de ter o Python instalado.

Clone o repositório:

```bash
git clone SEU_LINK_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd robo-cotacoes
```

Instale as dependências:

```bash
pip install requests streamlit
```

## ▶️ Como executar

### Versão pelo terminal

Execute:

```bash
python robo.py
```

Será apresentado um menu interativo para consultar as cotações, verificar alertas e visualizar o histórico.

### Versão Web

Para executar a aplicação com Streamlit:

```bash
streamlit run app.py
```

Após executar o comando, o Streamlit disponibilizará a aplicação no navegador.

## 🔄 Fluxo da aplicação

```text
              ┌──────────────────┐
              │      Usuário     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Python /         │
              │ Streamlit        │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     Requests     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   AwesomeAPI    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Dados em JSON    │
              └────────┬─────────┘
                       │
              ┌────────┴─────────┐
              ▼                  ▼
       ┌──────────────┐   ┌───────────────┐
       │ Cotações     │   │ Histórico     │
       │ atuais       │   │ .txt          │
       └──────────────┘   └───────────────┘
              │
              ▼
       ┌──────────────┐
       │ Alerta de    │
       │ preço        │
       └──────────────┘
```

## 🎯 Conceitos praticados

O desenvolvimento deste projeto permitiu praticar diferentes conceitos de Python e desenvolvimento de aplicações:

* Consumo de APIs REST.
* Requisições HTTP com `requests`.
* Manipulação de dados JSON.
* Criação e utilização de funções.
* Estruturas condicionais.
* Dicionários.
* Tratamento de arquivos.
* Manipulação de datas e horários.
* Validação de dados.
* Tratamento de erros.
* Interface web com Streamlit.
* Organização de código.
* Automação da consulta de informações externas.

## 📈 Melhorias futuras

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Criar gráficos com o histórico das cotações.
* [ ] Utilizar `pandas` para análise dos dados.
* [ ] Armazenar o histórico em SQLite ou outro banco de dados.
* [ ] Permitir a escolha de diferentes moedas.
* [ ] Criar alertas automáticos.
* [ ] Enviar notificações quando uma cotação atingir o preço definido.
* [ ] Adicionar atualização automática das cotações.
* [ ] Melhorar o tratamento de erros da API.
* [ ] Separar a aplicação em módulos.
* [ ] Criar testes automatizados.
* [ ] Adicionar um arquivo `requirements.txt`.

## 🎯 Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em **Python**, com foco em desenvolver aplicações práticas e entender como diferentes tecnologias podem ser integradas.

Através dele, pude trabalhar com **APIs, manipulação de dados, arquivos, lógica de programação e criação de interfaces web**, transformando dados externos em uma aplicação interativa e funcional.

## 👨‍💻 Autor

**Giliarde Rodrigues**

Estudante de Engenharia de Software | Python | Automação | Desenvolvimento de Software

---

⭐ Projeto desenvolvido para prática e aprendizado de Python, consumo de APIs e desenvolvimento de aplicações web.
