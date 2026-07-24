#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import sys


BANCO = "dados/hbv.db"


def converter(valor):

    if valor is None:
        return None

    valor = valor.strip()

    if valor in ["--", "-", ""]:
        return None

    multiplicador = 1

    if valor.endswith(" B"):
        valor = valor.replace(" B", "")
        multiplicador = 1000000000

    elif valor.endswith(" M"):
        valor = valor.replace(" M", "")
        multiplicador = 1000000

    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")

    try:
        return float(valor) * multiplicador

    except:
        return None


def periodo_tipo(periodo):

    if "T" in periodo:
        return "TRIMESTRAL"

    if periodo.isdigit():
        return "ANUAL"

    return "OUTRO"


def coletar(ticker):

    ticker = ticker.upper()

    url = f"https://www.dadosdemercado.com.br/acoes/{ticker.lower()}"

    html = requests.get(
        url,
        headers={"User-Agent":"Mozilla/5.0"}
    ).text

    soup = BeautifulSoup(html, "html.parser")

    tabelas = soup.find_all("table")

    if len(tabelas) < 5:
        print("Tabela não encontrada")
        return


    tabela = tabelas[4]

    linhas = tabela.find_all("tr")


    cabecalho = []

    for th in linhas[0].find_all(["th","td"]):
        cabecalho.append(
            th.get_text(" ",strip=True)
        )


    periodos = cabecalho[1:]


    conn = sqlite3.connect(BANCO)


    inseridos = 0


    for linha in linhas[1:]:

        colunas = [
            x.get_text(" ",strip=True)
            for x in linha.find_all(["td","th"])
        ]


        if len(colunas) < 2:
            continue


        conta = colunas[0]

        valores = colunas[1:]


        for periodo,valor in zip(periodos,valores):

            dados = {

                "receita_liquida": None,
                "lucro_liquido": None,
                "patrimonio": None,
                "margem_liquida": None,
                "roe": None,
                "dividendos": None

            }


            if conta == "Receita líquida":
                dados["receita_liquida"] = converter(valor)

            elif conta == "Lucro líquido":
                dados["lucro_liquido"] = converter(valor)

            elif conta == "Patrimônio líquido":
                dados["patrimonio"] = converter(valor)

            elif conta == "Margem líquida":
                dados["margem_liquida"] = converter(valor)

            elif conta == "ROE":
                dados["roe"] = converter(valor)

            else:
                continue


            conn.execute(
            """
            INSERT INTO indicadores_historico
            (
            ticker,
            periodo,
            tipo_periodo,

            receita_liquida,
            lucro_liquido,
            patrimonio,
            margem_liquida,
            roe,

            fonte,
            data_coleta
            )

            VALUES
            (?,?,?,?,?,?,?,?,?,?)

            """,

            (

            ticker,
            periodo,
            periodo_tipo(periodo),

            dados["receita_liquida"],
            dados["lucro_liquido"],
            dados["patrimonio"],
            dados["margem_liquida"],
            dados["roe"],

            "Dados de Mercado",
            datetime.now().date()

            )

            )


            inseridos += 1


    conn.commit()
    conn.close()


    print("="*60)
    print("COLETOR HISTORICO HBV")
    print(ticker)
    print(datetime.now())
    print("="*60)
    print("Registros inseridos:", inseridos)
    print("="*60)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso:")
        print("python coletar_indicadores_historico.py BBAS3")
        sys.exit()


    coletar(sys.argv[1])
