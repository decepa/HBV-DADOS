# MANUAL HBV
## Hunter Brasil Value

Versão: 1.0

Data inicial: 24/07/2026


# 1. OBJETIVO DO PROJETO

O HBV (Hunter Brasil Value) é um sistema de análise fundamentalista criado para identificar empresas brasileiras negociadas abaixo do valor justo.

O objetivo é criar um motor automático capaz de:

- coletar dados da bolsa;
- armazenar informações históricas;
- calcular indicadores;
- aplicar modelos de valuation;
- gerar ranking de oportunidades.


---

# 2. FILOSOFIA DO HBV

O HBV busca empresas com:

- qualidade;
- preço descontado;
- margem de segurança;
- histórico consistente;
- potencial de retorno.


O sistema não deve procurar apenas empresas baratas.

Uma empresa barata sem qualidade pode ser uma armadilha de valor.


---

# 3. REGRA PRINCIPAL DO PROJETO

## Não existe um modelo único para todas as empresas.

Cada setor deve possuir critérios e pesos próprios.


Motivo:

Bancos, energia, varejo, commodities e tecnologia possuem características diferentes.


---

# 4. REGRAS DE VALUATION


## 4.1 Graham

Utilizado principalmente para avaliar desconto em relação ao valor justo.


Critérios:

- lucro;
- patrimônio;
- segurança.


---

## 4.2 Bazin

Importante principalmente para empresas pagadoras de dividendos.


Critérios:

- dividend yield;
- histórico de pagamentos;
- previsibilidade.


---

## 4.3 Gordon

Utilizado como complemento.


Regra:

Gordon não deve dominar o modelo.

Terá peso menor que Graham e Bazin.


Motivo:

Modelos de crescimento possuem maior sensibilidade às premissas.


---

# 5. REGRAS POR SETOR


## Bancos

Prioridades:

- Graham;
- Bazin conservador;
- ROE;
- qualidade da carteira;
- inadimplência;
- crescimento do lucro.


Evitar:

- preço teto exageradamente otimista.


---

## Energia Elétrica

Prioridades:

- dividendos;
- geração de caixa;
- dívida;
- estabilidade dos contratos.


---

## Varejo

Prioridades:

- crescimento;
- margem;
- retorno sobre capital;
- endividamento.


---

## Commodities

Prioridades:

- ciclo da commodity;
- custo de produção;
- dívida;
- geração de caixa.


---

# 6. REGRAS DE DESENVOLVIMENTO


Antes de criar qualquer código novo:

1. verificar arquivos existentes;
2. verificar banco atual;
3. verificar tabelas existentes;
4. verificar manual;
5. registrar decisão.


Não criar estruturas duplicadas.


---

# 7. REGRAS DE DADOS


Dados originais nunca devem ser apagados.


Sempre guardar:

- fonte;
- data da coleta;
- arquivo original.


Toda coleta deve permitir reprodução futura.


---

# 8. BANCO DE DADOS ATUAL


Banco:

dados/hbv.db


Sistema:

SQLite


Tabela atual:


## acoes


Campos:


id

Identificador interno.


ticker

Código da ação.


nome

Nome da empresa.


setor

Classificação setorial.


---

# 9. FONTE ATUAL DE AÇÕES


Fonte:

Dados de Mercado


Página:

https://www.dadosdemercado.com.br/acoes


Arquivo:

dados/acoes_dadosmercado.csv


Quantidade atual:

374 ações cadastradas.


---

# 10. ESTRUTURA PLANEJADA


## Tabela cotacoes

Guardar:

- preço;
- data;
- volume;
- histórico.


## Tabela indicadores

Guardar:

- lucro;
- dividendos;
- ROE;
- margem;
- dívida;
- crescimento.


## Tabela valuation

Guardar:

- Graham;
- Bazin;
- Gordon;
- preço justo;
- desconto.


## Tabela ranking_hbv

Resultado final.


---

# 11. FLUXO FINAL DO SISTEMA


Coleta de dados

↓

Banco HBV

↓

Indicadores

↓

Valuation

↓

Ranking

↓

Relatório diário


---

# 12. REGRAS DE CONTROLE


Toda alteração importante deve gerar:

1. atualização deste manual;
2. registro no DIARIO.md;
3. novo commit no GitHub.


---

# 13. ESTADO ATUAL


Concluído:

[X] Banco criado

[X] Lista de ações criada

[X] 374 empresas cadastradas

[X] Setores cadastrados

[X] Documentação inicial criada


Próxima etapa:

Criar módulo de cotações.


---

# FIM DO MANUAL HBV
---

# 14. REGRA DE ATUALIZAÇÃO DO DIÁRIO

Sempre que uma alteração precisar ser registrada no diário do projeto:

1. Informar o comando completo para edição do arquivo.

2. Informar exatamente onde adicionar o conteúdo.

3. Informar o procedimento de salvamento.

4. Informar o comando de conferência do arquivo.

5. Informar os comandos completos para commit e envio ao GitHub.


Padrão obrigatório:

- nunca enviar somente o texto a ser colado;
- sempre enviar o passo a passo completo;
- manter o histórico do projeto rastreável no GitHub.


Objetivo:

Evitar perda de informações e manter a documentação do HBV sincronizada com o desenvolvimento.

---

# 14. REGRA DE ATUALIZAÇÃO DO DIÁRIO

Sempre que uma alteração precisar ser registrada no diário do projeto:

1. Informar o comando completo para edição do arquivo.

2. Informar exatamente onde adicionar o conteúdo.

3. Informar o procedimento de salvamento.

4. Informar o comando de conferência do arquivo.

5. Informar os comandos completos para commit e envio ao GitHub.


Padrão obrigatório:

- nunca enviar somente o texto a ser colado;
- sempre enviar o passo a passo completo;
- manter o histórico do projeto rastreável no GitHub.


Objetivo:

Evitar perda de informações e manter a documentação do HBV sincronizada com o desenvolvimento.
