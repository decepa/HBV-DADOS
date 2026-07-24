import sqlite3
import os

BANCO = "banco/hbv_dados.db"

os.makedirs("banco", exist_ok=True)

conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

# Cadastro das empresas
cursor.execute("""
CREATE TABLE IF NOT EXISTS empresas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT UNIQUE,
    razao_social TEXT,
    nome_fantasia TEXT,
    setor TEXT,
    subsetor TEXT,
    segmento TEXT,
    tipo_empresa TEXT,
    data_ipo TEXT
)
""")

# Histórico de cotações
cursor.execute("""
CREATE TABLE IF NOT EXISTS cotacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    data TEXT,
    preco_abertura REAL,
    preco_maximo REAL,
    preco_minimo REAL,
    preco_fechamento REAL,
    volume_financeiro REAL,
    quantidade_negociada REAL,
    valor_mercado REAL,
    numero_acoes REAL,
    free_float REAL
)
""")

# Dados financeiros
cursor.execute("""
CREATE TABLE IF NOT EXISTS fundamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    periodo TEXT,
    receita_liquida REAL,
    lucro_liquido REAL,
    ebitda REAL,
    patrimonio_liquido REAL,
    divida_liquida REAL,
    roe REAL,
    roic REAL,
    margem_liquida REAL
)
""")

# Dividendos
cursor.execute("""
CREATE TABLE IF NOT EXISTS dividendos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    data_pagamento TEXT,
    dividendo REAL,
    jcp REAL,
    dividendo_por_acao REAL,
    dividend_yield REAL
)
""")

# Indicadores
cursor.execute("""
CREATE TABLE IF NOT EXISTS indicadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    data TEXT,
    pl REAL,
    pvp REAL,
    ev_ebitda REAL,
    ev_ebit REAL,
    p_fcf REAL,
    market_cap REAL,
    enterprise_value REAL
)
""")

# Eventos
cursor.execute("""
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT,
    data TEXT,
    tipo_evento TEXT,
    descricao TEXT
)
""")

conexao.commit()
conexao.close()

print("Banco HBV-DADOS criado com sucesso!")
