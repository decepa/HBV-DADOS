# Diário de Desenvolvimento - HBV

## 24/07/2026

# Objetivo do dia

Estruturar a base inicial do projeto HBV, criando uma base confiável de empresas da B3 e preparando o banco para receber o motor de valuation.

---

# 1. Estrutura inicial

Projeto criado:

HBV-DADOS

Banco principal:

dados/hbv.db

Banco utilizado:

SQLite

---

# 2. Criação da tabela de ações

Tabela:

acoes

Campos:

- id
- ticker
- nome
- segmento
- setor

---

# 3. Captura da lista de ações

Fonte utilizada:

Dados de Mercado

Página pública:

https://www.dadosdemercado.com.br/acoes


Arquivo gerado:

dados/acoes_dadosmercado.csv


Resultado:

374 ações importadas.


Validação realizada:

SELECT COUNT(*) FROM acoes;


Resultado:

374


---

# 4. Limpeza da base

Foram descartados:

- ativos fracionários
- ETFs
- códigos não desejados
- duplicidades


A base final ficou com ações negociadas normalmente.

---

# 5. Classificação setorial

Foi utilizada a classificação oficial encontrada nas páginas individuais das ações.


Campo coletado:

Classificação setorial


Exemplos:


BBAS3

Financeiro / Intermediários Financeiros / Bancos


PETR4

Petróleo, Gás e Biocombustíveis


TAEE11

Utilidade Pública / Energia Elétrica


WEGE3

Bens Industriais / Máquinas e Equipamentos


---

# 6. Decisões do projeto

## Manter setor original

A classificação detalhada será mantida.

Não será simplificada agora.

Motivo:

Permitir análises futuras mais precisas por indústria.


---

# 7. Estado atual

Banco:

dados/hbv.db


Ativos cadastrados:

374


Informações disponíveis:

- ticker
- nome
- setor oficial B3


---

# Próximas etapas

1. Captura de cotações.
2. Cadastro de indicadores fundamentalistas.
3. Criar tabela financeira.
4. Criar motor Graham.
5. Criar motor Bazin.
6. Criar Gordon.
7. Criar ranking HBV.
8. Criar relatório diário automático.


---

# Observação

Todas as alterações futuras devem ser registradas neste arquivo.
---

## 24/07/2026 - Módulo de cotações

Coletor criado:

scripts/atualizar_cotacoes.py


Fonte utilizada:

Yahoo Finance


Resultado do primeiro processamento:

374 ativos analisados

371 cotações coletadas


Ativos sem dados na fonte:

- AZEV11
- BHIA3
- BIOM11
- NGRD3


Diagnóstico:

Os ativos permanecem cadastrados na base.

A ausência de cotação ocorre por falta de dados disponíveis na fonte Yahoo Finance.


Decisão:

Não remover ativos da tabela acoes.

A base oficial deve preservar todos os ativos cadastrados.


Próxima etapa:

Criar módulo de indicadores fundamentalistas.
---

## 24/07/2026 - Início módulo de indicadores

Verificação realizada:

- tabela indicadores existente;
- tabela sem registros;
- não existem scripts de fundamentos.

Decisão:

Criar novo módulo:

scripts/coletar_indicadores.py


Objetivo:

Popular a tabela indicadores com dados fundamentalistas para alimentar:

- Graham;
- Bazin;
- Gordon;
- Ranking HBV.


Campos planejados:

- PL
- PVP
- DY
- ROE
- ROIC
- Margem líquida
- Margem EBIT
- Dívida líquida/EBITDA
- Lucro 12 meses
- Receita 12 meses


Próxima etapa:

Definir fonte pública de fundamentos e iniciar coleta.
