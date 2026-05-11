# 📊 ETL de Cotação de Moedas (USD → BRL)

---

## 🚀 Objetivo e Contexto

Projeto de Engenharia de Dados desenvolvido em Python que realiza:

- Extração de dados atuais de cotação via API pública
- Armazenamento histórico em banco de dados (SQL Server)
- Cálculo de variações (percentual e absoluta) baseada no histórico de dados, comparando a cotação atual com o valor anterior
- Exportação para Excel para análises e dashboards

---

## 🧰 Tecnologias Utilizadas

- Python
- Pandas
- Requests
- SQLAlchemy
- SQL Server
- Git / GitHub

---

## 📥 Fonte de Dados

API pública de câmbio:

https://open.er-api.com/v6/latest/USD

### ⏰ Atualização dos dados

A API é atualizada diariamente por volta de 00:00 UTC (aprox. 21:00 no horário de Brasília).

Execuções após esse horário podem retornar dados do dia seguinte.

---

## ▶️ Como Executar (Siga todos os passos)

### 1. Clone o repositório ou baixe os arquivos 

git clone https: https://github.com/guilherme-viana-silva/cotacao-BRL-USD.git
cd etl-cotacoes

---

### 2. Criar ambiente virtual ,abra o terminal e execute: 

python -m venv "NOME_DO_AMBIENTE_VIRTUAL"

---

### 3. Ativar ambiente virtual

"NOME_DO_AMBIENTE_VIRTUAL"\Scripts\activate  

---

### 4. Instalar dependências

pip install -r requirements.txt

---

### 5. Configurar credenciais SQL Server

Altere no código usando suas credenciais do SQL Server:

- server   
- username  
- password  

---

### 6. Criar o Banco de Dados e Tabela

 - Execute o comando transact.sql que se encontra dentro da pasta ‘01_projeto’ .
(Copie e cole e execute no seu Sql server)

### 7. Executar o projeto

python cotacao.py

---

### ⚠️ Observações

A api fornece apenas dados diários da cotação, por isso, o script só deve ser executado uma vez por dia a fins de manter um histórico de dados no SQL Server limpo de itens duplicados.

A coluna data é única para evitar duplicidade.
Se o script rodar mais de uma vez no mesmo dia, a inserção será ignorada.

Isso pode gerar lacunas no id (ex: 1, 3, 4...), o que é normal e não impacta o sistema.
Use a data como referência nas consultas.

Os primeiros dados de variação sempre serão nulos, pois não possuem histórico de cotação no banco de dados para comparação de métricas. 


### 🤖Automação 

Para uma melhor experiência com o projeto, o script pode ser colocado no agendamento de tarefas do Windows para execução diária.

---

## 👨‍💻 Autor

- Guilherme Viana Pereira da Silva  
- Projeto desenvolvido para fins de estudo em Engenharia de dados.
