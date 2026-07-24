# MODELO BANCO HBV-DADOS

## Objetivo

Criar uma base completa de dados financeiros e de mercado para alimentar o HBV-ENGINE.

O HBV-DADOS será responsável apenas pela coleta, organização e armazenamento dos dados.

O cálculo de valuation ficará separado no HBV-ENGINE.

---

# Estrutura de dados

## 1. Empresas

Cadastro principal.

Campos:

- ticker
- razao_social
- nome_fantasia
- setor
- subsetor
- segmento
- tipo_empresa
- data_ipo

---

## 2. Cotações

Histórico de mercado.

Campos:

- ticker
- data
- preco_abertura
- preco_maximo
- preco_minimo
- preco_fechamento
- volume_financeiro
- quantidade_negociada
- valor_mercado
- numero_acoes
- free_float

---

## 3. Demonstrações financeiras

DRE anual e trimestral.

Campos:

- periodo
- receita_liquida
- crescimento_receita
- lucro_bruto
- EBIT
- EBITDA
- lucro_liquido
- lucro_por_acao
- margem_bruta
- margem_ebitda
- margem_liquida

---

## 4. Balanço patrimonial

Campos:

- ativo_total
- ativo_circulante
- passivo_total
- passivo_circulante
- patrimonio_liquido
- caixa
- investimentos
- imobilizado
- intangivel

---

## 5. Endividamento

Campos:

- divida_bruta
- divida_liquida
- divida_curto_prazo
- divida_longo_prazo
- caixa
- divida_liquida_ebitda
- divida_patrimonio

---

## 6. Fluxo de caixa

Campos:

- fluxo_caixa_operacional
- fluxo_caixa_investimento
- fluxo_caixa_financiamento
- fluxo_caixa_livre

---

## 7. Dividendos

Base para Bazin.

Campos:

- data_pagamento
- dividendo
- JCP
- dividendo_por_acao
- dividend_yield
- dy_5_anos
- dy_10_anos

---

## 8. Indicadores de mercado

Campos:

- P/L
- P/VP
- EV/EBITDA
- EV/EBIT
- P/FCF
- market_cap
- enterprise_value

---

## 9. Indicadores de qualidade

Campos:

- ROE
- ROIC
- ROA
- margem_bruta
- margem_liquida
- crescimento_lucro_5anos
- crescimento_receita_5anos

---

# Dados específicos por setor

## Bancos

- basileia
- inadimplencia
- carteira_credito
- provisoes
- lucro_recorrente

## Seguros

- premios_emitidos
- sinistralidade
- resultado_financeiro

## Energia

- capacidade_instalada
- energia_gerada
- contratos
- divida_ebitda

## Commodities

- producao
- preco_commodity
- custo_operacional

## Varejo

- mesmas_lojas
- numero_lojas
- margem_bruta
- estoque

---

# Governança e risco

Campos:

- nivel_governanca
- novo_mercado
- controle_estatal
- rating_divida

---

# Eventos

Histórico de acontecimentos.

Campos:

- ticker
- data
- tipo_evento
- descricao

Tipos:

- resultado
- dividendos
- grupamento
- desdobramento
- fato relevante

---

# Próxima etapa

Criar o banco SQLite baseado neste modelo.
