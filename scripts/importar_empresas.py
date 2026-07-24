import sqlite3
import csv
import os

BANCO = "banco/hbv_dados.db"
ARQUIVO = "tabelas/empresas.csv"

os.makedirs("tabelas", exist_ok=True)

conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

if not os.path.exists(ARQUIVO):
    print("Arquivo empresas.csv não encontrado")
    print("Crie o arquivo em:", ARQUIVO)
    conexao.close()
    exit()

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    total = 0

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

print(f"{total} empresas importadas com sucesso!")
