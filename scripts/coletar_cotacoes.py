import sqlite3
import yfinance as yf
from datetime import datetime

BANCO = "banco/hbv_dados.db"


def buscar_empresas(cursor):
    cursor.execute("""
        SELECT ticker
        FROM empresas
        ORDER BY ticker
    """)

    return [linha[0] for linha in cursor.fetchall()]


def salvar_cotacao(cursor, dados):
    cursor.execute("""
    INSERT OR REPLACE INTO cotacoes
    (
        ticker,
        data,
        preco_abertura,
        preco_maximo,
        preco_minimo,
        preco_fechamento,
        volume_financeiro
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, dados)


conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

acoes = buscar_empresas(cursor)

print("=" * 50)
print("COLETA DE COTAÇÕES HBV-DADOS")
print(datetime.now())
print("=" * 50)


for ticker in acoes:

    ativo = ticker + ".SA"

    print(f"Coletando {ticker}...")

    try:

        dados = yf.download(
            ativo,
            period="5d",
            progress=False,
            auto_adjust=False
        )

        if dados.empty:
            print(f"{ticker} sem dados")
            continue


        ultimo = dados.iloc[-1]

        data = dados.index[-1].strftime("%Y-%m-%d")

        abertura = float(ultimo["Open"].iloc[0])
        maxima = float(ultimo["High"].iloc[0])
        minima = float(ultimo["Low"].iloc[0])
        fechamento = float(ultimo["Close"].iloc[0])
        volume = float(ultimo["Volume"].iloc[0])


        salvar_cotacao(
            cursor,
            (
                ticker,
                data,
                abertura,
                maxima,
                minima,
                fechamento,
                volume
            )
        )


        print(f"{ticker} OK - R$ {fechamento:.2f}")


    except Exception as erro:

        print(f"{ticker} ERRO: {erro}")


conexao.commit()
conexao.close()


print("=" * 50)
print("COLETA FINALIZADA")
print("=" * 50)
