#!/usr/bin/env python3

import sqlite3


BANCO = "dados/hbv.db"


conn = sqlite3.connect(BANCO)


conn.execute("""
CREATE TABLE IF NOT EXISTS indicadores_historico (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    ticker TEXT,
    periodo TEXT,
    tipo_periodo TEXT,

    lucro_liquido REAL,
    receita_liquida REAL,

    roe REAL,
    roic REAL,

    margem_liquida REAL,
    margem_ebit REAL,

    divida_liquida REAL,

    patrimonio REAL,

    dividendos REAL,

    fonte TEXT,
    data_coleta DATE
)
""")


conn.commit()

print("="*50)
print("HBV - TABELA HISTORICO INDICADORES")
print("Criada com sucesso")
print("="*50)


conn.close()
