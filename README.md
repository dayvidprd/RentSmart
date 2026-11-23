# RentSmart

## Sobre o projeto

RentSmart é um projeto desenvolvido em Python para simular um sistema de orçamento de locação de imóveis.

A ideia é permitir que o usuário escolha um tipo de imóvel, forneça algumas características e visualize o valor da locação, incluindo os possíveis adicionais e a taxa contratual.

O sistema gera um arquivo CSV com a projeção dos valores durante 12 meses, facilitando a visualização dos gastos.

Esse projeto foi desenvolvido como atividade da faculdade, com o objetivo de colocar em prática os conhecimentos que estamos aprendendo em programação.

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos (POO)
- Arquivos CSV
- Git e GitHub

## O que o sistema faz?

Atualmente, o RentSmart possui algumas funcionalidades:

- Escolha entre apartamento, casa ou studio.
- Seleção da quantidade de quartos.
- Opção de garagem e vagas adicionais.
- Cálculo do valor do aluguel conforme as escolhas.
- Aplicação de descontos quando disponíveis.
- Cálculo da taxa contratual, com opção de parcelamento.
- Geração de uma planilha CSV com a projeção dos próximos 12 meses.

## Como executar

Para executar o projeto, é necessário ter o Python instalado no computador.

**1.** Primeiro, baixe o repositório pelo GitHub ou utilize o comando:

```bash
git clone https://github.com/dayvidprd/RentSmart.git
```

**2.** Entre na pasta do projeto:

```bash
cd RentSmart
```

**3.** Execute o programa:

```bash
python rentsmart.py
```

Caso esteja utilizando Windows e não funcione, também é possível tentar:

```bash
py rentsmart.py
```

Depois disso, basta seguir as opções que aparecem no terminal e preencher as informações solicitadas pelo programa.

## Arquivos do projeto

| Arquivo                           | Para que serve                           |
| --------------------------------- | ---------------------------------------- |
| `rentsmart.py`                    | Código principal do sistema.             |
| `projecao_rentsmart.csv`          | Arquivo com a projeção financeira.       |
| `Relatorio_Teorico_RentSmart.pdf` | Relatório com as informações do projeto. |
| `evidencias.zip`                  | Prints e registros do desenvolvimento.   |

## O que foi utilizado na programação?

Durante o desenvolvimento, foram aplicados alguns conceitos estudados na faculdade, como:

- Classes e objetos;
- Atributos e métodos;
- Estruturas condicionais (`if`, `elif` e `else`);
- Estruturas de repetição;
- Validação de informações;
- Tratamento de erros;
- Manipulação e geração de arquivos CSV.
