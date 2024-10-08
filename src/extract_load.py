# imports
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# imports de variáveis de ambiente

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

#DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
DATABASE_URL = 'postgresql://postgres123:pz1W4QNyMVXmGwPPBD6yK1uEcVrCgfVm@dpg-crednb3gbbvc73bq96cg-a.oregon-postgres.render.com/dbsales_i55p'

engine = create_engine(DATABASE_URL)

def buscar_dados_commodities(simbolo,periodo='5d',intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period = periodo, interval = intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_comodities(commodities):
    todos_dados = []
    for simbolos in commodities:
        dados = buscar_dados_commodities(simbolos)
        todos_dados.append(dados)

    return pd.concat(todos_dados)


def salvar_no_postgres(df,schema = 'public'):
    df.to_sql('commodities',engine, if_exists = 'replace',index = True,index_label='Date',schema=schema)

if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_comodities(commodities)
    salvar_no_postgres(dados_concatenados,schema='public')

# pegar as cotações do ativo



# concatenar os meus ativos (1...2....3) ----> (1)


# salvar no banco de dados


