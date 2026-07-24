import sqlite3
import csv
from datetime import datetime

BANCO = "banco/hbv_dados.db"
ARQUIVO = "tabelas/empresas_b3.csv"


conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()


print("=" * 50)
print("IMPORTAÇÃO EMPRESAS B3 - HBV-DADOS")
print(datetime.now())
print("=" * 50)


total = 0


with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

    leitor = csv.DictReader(arquivo)

    for empresa in leitor:

        cursor.execute("""
        INSERT OR REPLACE INTO empresas
        (
            ticker,
            razao_social,
            nome_fantasia,
            setor,
            subsetor,
            segmento,
            tipo_empresa
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            empresa["ticker"],
            empresa["razao_social"],
            empresa["nome_fantasia"],
            empresa["setor"],
            empresa["subsetor"],
            empresa["segmento"],
            empresa["tipo_empresa"]
        ))

        total += 1


conexao.commit()
conexao.close()


print("=" * 50)
print(f"{total} empresas importadas!")
print("=" * 50)
