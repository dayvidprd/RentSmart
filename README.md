# RentSmart – R.M Imóveis

## Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para automatizar o cálculo de orçamentos de locação de imóveis. O sistema permite calcular o aluguel de apartamentos, casas e studios, considerando quartos, vagas de garagem, descontos e taxas contratuais.

O objetivo é facilitar o cálculo dos valores, evitar erros manuais e gerar uma projeção financeira de 12 meses.

## Funcionalidades

- Seleção do tipo de imóvel.
- Cálculo de aluguel base e adicionais.
- Aplicação de desconto para apartamentos sem crianças.
- Cálculo da taxa contratual de R$ 2.000,00.
- Divisão da taxa contratual em até 5 parcelas.
- Validação das entradas do usuário.
- Exibição do resumo do orçamento.
- Geração de arquivo CSV com projeção de 12 meses.

## Regras de negócio

### Apartamento

- 1 quarto: R$ 700,00.
- 2 quartos: R$ 900,00.
- Vaga de garagem: adicional de R$ 300,00.
- Desconto de 5% para clientes sem crianças.

### Casa

- 1 quarto: R$ 900,00.
- 2 quartos: R$ 1.150,00.
- Vaga de garagem: adicional de R$ 300,00.

### Studio

- Valor base: R$ 1.200,00.
- Pacote inicial de vagas: R$ 250,00.
- Vagas adicionais: R$ 60,00 cada.

### Taxa contratual

- Valor total: R$ 2.000,00.
- Parcelamento permitido de 1 a 5 vezes.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- Biblioteca CSV

## Estrutura do projeto

RentSmart/
├── rentsmart.py
├── projecao_rentsmart.csv
├── README.md
├── Evidencias/
├── Relatorios/
└── Videos/

```

## Como executar

1. Instale o Python.
2. Baixe ou clone o repositório.
3. Abra a pasta do projeto no terminal.
4. Execute o comando:

5. Siga as instruções apresentadas no terminal.

## Arquivo CSV

O sistema gera automaticamente o arquivo `projecao_rentsmart.csv`, contendo:

- Mês.
- Valor do aluguel.
- Parcela contratual.
- Total mensal.

A projeção contempla 12 meses.

## Programação Orientada a Objetos

O sistema utiliza duas classes principais:

- `Imovel`: responsável por armazenar os dados do imóvel e calcular o aluguel.
- `Orcamento`: responsável pelo desconto, taxa contratual, resumo financeiro e geração do CSV.

Essa organização permite separar as responsabilidades e facilita a manutenção do código.

## Projeto acadêmico

Desenvolvido como atividade acadêmica de Pensamento Algorítmico e Introdução à Programação Orientada a Objetos.
    
