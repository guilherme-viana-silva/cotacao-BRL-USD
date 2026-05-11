import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine

url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(list(data["rates"].items()), columns=["moeda", "cotacao"])

df["data"] = data["time_last_update_utc"]
df["moeda_base"] = data["base_code"]

df["data"] = pd.to_datetime(df["data"]).dt.date

df_real = df.loc[df["moeda"] == "BRL"]

# preencha com suas credenciais do SQL Server.
server = 'SEU_SERVER'
database = 'finanças'
username = 'SEU_USUARIO'
password = 'SUA_SENHA'
conexaoDB = ('DRIVER={ODBC Driver 17 for SQL Server};'
             f'SERVER={server};'
             f'DATABASE={database};'
             f'UID={username};'
             f'PWD={password};'
             # 'Trusted_Connection=yes;'  # conexão usuario do windows caso prefira.
             )

engine = create_engine(f'mssql+pyodbc:///?odbc_connect={conexaoDB}')

df_real.to_sql(name='cotacao_real', con=engine,
               if_exists='append', index=False)

query = '''SELECT [id]
      ,[moeda]
      ,[cotacao]
      ,[data]
      ,[moeda_base]
  FROM [finanças].[dbo].[cotacao_real]'''

df_consulta = pd.read_sql(query, engine)

df_consulta["data"] = pd.to_datetime(df_consulta["data"])

df_consulta = df_consulta.sort_values(['moeda', 'data'])

df_consulta["variacao(%)"] = df_consulta.groupby(
    "moeda")["cotacao"].pct_change() * 100
df_consulta["variacao(N)"] = df_consulta.groupby("moeda")["cotacao"].diff()

df_consulta["variacao(%)"] = df_consulta["variacao(%)"].fillna(0)
df_consulta["variacao(N)"] = df_consulta["variacao(N)"].fillna(0)

# arredondar os dados de variação para melhor visualização.
df_consulta["variacao(%)"] = df_consulta["variacao(%)"].round(2)
df_consulta["variacao(N)"] = df_consulta["variacao(N)"].round(4)

df_consulta["data"] = df_consulta["data"].dt.strftime('%d/%m/%Y')

horario_atual = datetime.now().strftime("%d-%m-%y_%H-%M")

df_consulta.to_excel(
    f"02_arquivos_excel/cotacoes_real_{horario_atual}.xlsx", index=False, sheet_name='variacao_financeira')

engine.dispose()
