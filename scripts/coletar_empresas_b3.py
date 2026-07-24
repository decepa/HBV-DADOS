import sqlite3
import yfinance as yf
from datetime import datetime


BANCO = "banco/hbv_dados.db"


def buscar_tickers():

    print("Buscando lista de empresas B3...")

    tickers = [
        "ABEV3",
        "BBAS3",
        "BBSE3",
        "ITSA4",
        "PETR4",
        "VALE3",
        "WEGE3",
        "POMO3",
        "EGIE3",
        "TAEE11"
    ]

    return tickers



def salvar_empresa(cursor, ticker):

    nome = ticker
    setor = ""
    segmento = ""

    try:

        empresa = yf.Ticker(ticker + ".SA")

        info = empresa.info

        nome = info.get(
            "longName",
            ticker
        )

        setor = info.get(
            "sector",
            ""
        )

        segmento = info.get(
            "industry",
            ""
        )

    except Exception as erro:

        print("Erro dados", ticker, erro)


    cursor.execute("""
    INSERT OR REPLACE INTO empresas
    (
        ticker,
        nome_fantasia,
        setor,
        segmento
    )
    VALUES (?,?,?,?)
    """,
    (
        ticker,
        nome,
        setor,
        segmento
    ))



conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()


print("="*50)
print("COLETA AUTOMATICA EMPRESAS B3")
print(datetime.now())
print("="*50)


tickers = buscar_tickers()


for ticker in tickers:

    print("Importando", ticker)

    salvar_empresa(
        cursor,
        ticker
    )


conexao.commit()
conexao.close()


print("="*50)
print("EMPRESAS ATUALIZADAS")
print("="*50)
