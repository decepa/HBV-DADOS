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
---

## 24/07/2026 - Mapeamento de indicadores concluído

Teste realizado:

Ativo:
BBAS3


Fonte analisada:

Dados de Mercado


Indicadores encontrados no HTML:

- P/L
- P/VP
- ROE
- ROIC
- Margem líquida
- Receita líquida
- Lucro líquido
- Dados históricos


Decisão:

Utilizar o Dados de Mercado como fonte inicial para coleta de indicadores fundamentalistas.


Próxima etapa:

Criar script de teste para extração dos indicadores de uma ação antes da gravação no banco.
---

## 24/07/2026 - Decisão arquitetura indicadores históricos

Análise realizada:

Para cálculo de preço teto projetado, apenas o indicador atual não é suficiente.


Decisão:

Manter a tabela indicadores como snapshot atual.

Criar uma estrutura histórica para armazenar evolução trimestral e anual.


Objetivo:

Permitir projeções de:

- Graham;
- Bazin;
- Gordon;
- crescimento de lucro;
- crescimento de dividendos;
- preço teto HBV.


Dados históricos planejados:

- lucro líquido;
- receita líquida;
- ROE;
- ROIC;
- margens;
- dívida;
- patrimônio;
- dividendos.


Motivo:

O HBV precisa analisar qualidade e crescimento, não apenas preço atual.


Próxima etapa:

Criar tabela indicadores_historico.
---

## 24/07/2026 - Criada tabela indicadores_historico

Alteração realizada:

Criada nova tabela:

indicadores_historico


Objetivo:

Armazenar evolução trimestral e anual dos fundamentos das empresas.


Campos armazenados:

- lucro líquido;
- receita líquida;
- ROE;
- ROIC;
- margens;
- dívida;
- patrimônio;
- dividendos;
- fonte;
- data da coleta.


Motivo:

Permitir projeções de preço teto utilizando histórico de resultados.


Status:

Tabela criada e validada no SQLite.


Próxima etapa:

Criar coletor de indicadores históricos.
---

## 24/07/2026 - Análise estrutura histórico Dados de Mercado

Foi realizado teste de extração da página individual das ações.

Ticker testado:

BBAS3


Resultado:

Foram encontradas 8 tabelas HTML.


Identificadas:


Tabela 0:

Indicadores anuais.

Dados encontrados:

- P/L
- P/VP
- PSR
- LPA
- VPA
- ROE
- margens


Tabela 2:

Histórico trimestral patrimonial.


Tabela 4:

Histórico trimestral de resultados.


Decisão:

O coletor histórico utilizará as tabelas trimestrais e anuais para alimentar:

indicadores_historico


Objetivo:

Permitir cálculo de:

- crescimento de lucro;
- média histórica;
- projeções;
- preço teto HBV;
- margem de segurança.


Próxima etapa:

Criar coletor automático de indicadores históricos.
---

## 24/07/2026 - Primeiro teste coletor histórico indicadores

Criado:

scripts/coletar_indicadores_historico.py


Teste realizado:

Ticker:

BBAS3


Resultado:

65 registros inseridos na tabela:

indicadores_historico


Dados coletados:

- Receita líquida trimestral
- Períodos históricos


Validação:

SELECT COUNT(*) FROM indicadores_historico;

Resultado:

65 registros


Observações encontradas:

Alguns períodos precisam tratamento:

- valores anuais aparecem misturados com dados trimestrais;
- alguns campos retornam zero;
- será necessário validar tipo_periodo antes da coleta definitiva.


Decisão:

Não expandir para todas as ações ainda.

Primeiro corrigir tratamento dos períodos.


Próxima etapa:

Ajustar coletor histórico para separar:

- trimestre;
- ano;
- TTM.
---

## 24/07/2026 - Padronização de períodos históricos

Durante o primeiro teste do coletor de indicadores históricos da BBAS3 foram identificados períodos de diferentes naturezas na mesma fonte.

Foram encontrados:

- períodos trimestrais;
- períodos anuais;
- períodos TTM.

Decisão do projeto:

A tabela indicadores_historico deverá armazenar o tipo do período corretamente.

Classificações:

TRIMESTRAL:
- 1T2026
- 2T2025
- 3T2025
- 4T2025

ANUAL:
- 2025
- 2024
- 2023

TTM:
- períodos acumulados dos últimos 12 meses.


Motivo:

O motor HBV utilizará os dados históricos para:

- projeção de lucro;
- crescimento;
- preço teto;
- Graham;
- Bazin;
- Gordon.


Regra:

Nunca misturar dados trimestrais com anuais nos cálculos de valuation.


Próxima etapa:

Ajustar coletor histórico para identificar automaticamente o tipo_periodo antes da gravação no banco.
