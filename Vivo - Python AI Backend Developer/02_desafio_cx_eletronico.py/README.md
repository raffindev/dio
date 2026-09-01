# 🏦 Sistema Bancário Modular

Segundo desafio desenvolvido durante a formação **Vivo — Python AI Backend Developer**, da [DIO](https://www.dio.me/).

O projeto consiste na implementação de um **sistema bancário executado via terminal**, permitindo cadastrar usuários, criar e acessar contas correntes e realizar operações bancárias.

A solução foi desenvolvida de forma modular, separando as responsabilidades da aplicação em diferentes arquivos e utilizando **JSON para persistência dos dados**.

---

## 🎯 Objetivo

Aplicar os fundamentos de Python em uma aplicação mais próxima de um sistema real, trabalhando não apenas a lógica de programação, mas também conceitos de:

* Modularização
* Funções
* Validação de dados
* Manipulação de arquivos
* Persistência de informações
* Estruturas de dados
* Organização de responsabilidades

---

## ⚙️ Funcionalidades

### 👤 Usuários

O sistema permite:

* Cadastrar novos usuários
* Buscar usuários pelo CPF
* Validar CPF
* Impedir o cadastro de CPF duplicado
* Registrar nome completo
* Registrar data de nascimento
* Validar datas utilizando `datetime.date`
* Impedir datas de nascimento futuras
* Registrar endereço completo

Os dados do usuário são armazenados em `usuario.json`.

---

### 💳 Conta Corrente

Cada usuário pode:

* Criar uma conta corrente
* Informar o número da conta para acesso
* Validar se a conta pertence ao usuário autenticado
* Consultar sua conta corrente

As contas são armazenadas em `contas.json`.

---

### 💰 Operações Bancárias

Após acessar uma conta, o usuário pode:

#### Depósito

* Realizar depósitos
* Impedir valores menores ou iguais a zero
* Atualizar o saldo
* Registrar a operação no extrato

#### Saque

* Realizar saques
* Impedir valores inválidos
* Verificar saldo disponível
* Aplicar limite de **R$ 500,00 por saque**
* Aplicar limite de **3 saques por sessão**
* Atualizar o saldo
* Registrar a operação no extrato

#### Extrato

O sistema apresenta:

* Saldo atual
* Histórico das operações realizadas durante a sessão
* Numeração das operações

---

## 🧩 Arquitetura

O projeto foi dividido em módulos de acordo com a responsabilidade de cada parte:

```text
02_desafio_cx_eletronico.py/
│
├── main.py
│
├── usuario.py
│
├── contas.py
│
├── cx_eletronico.py
│
└── dados/
    ├── usuario.json
    └── contas.json
```

### `main.py`

Responsável por iniciar e conectar o fluxo principal da aplicação.

```text
iniciar_caixa()
      ↓
menu_conta_corrente()
      ↓
menu_caixa_eletronico()
```

---

### `usuario.py`

Concentra as funcionalidades relacionadas aos usuários.

Principais responsabilidades:

* `criar_usuario()`
* `buscar_usuario()`

Também realiza validações de CPF, data de nascimento e endereço, além de persistir os usuários no arquivo JSON.

---

### `contas.py`

Responsável pelo gerenciamento das contas correntes.

Principais responsabilidades:

* `criar_conta_corrente()`
* `buscar_conta_corrente()`
* `menu_conta_corrente()`

A busca da conta considera tanto o número da conta quanto o CPF do usuário, evitando que uma conta pertencente a outro usuário seja acessada.

---

### `cx_eletronico.py`

Concentra as operações realizadas dentro do caixa eletrônico.

Principais funções:

* `iniciar_caixa()`
* `depositar()`
* `sacar()`
* `exibir_extrato()`
* `menu_caixa_eletronico()`

---

## 💾 Persistência de Dados

O projeto utiliza arquivos **JSON** como uma forma simples de persistir os dados entre execuções.

```text
dados/
│
├── usuario.json
└── contas.json
```

Os dados são carregados durante a inicialização e atualizados ao realizar alterações.

A escolha do JSON permite trabalhar, na prática, com:

* leitura de arquivos;
* escrita de arquivos;
* serialização de dados;
* listas e dicionários;
* persistência de informações.

---

## 🧠 Conceitos de Python Praticados

Este desafio permitiu aplicar diversos recursos da linguagem:

### Fundamentos

* Variáveis
* Tipos de dados
* `input()`
* `print()`
* Operadores
* `if / elif / else`
* `while`
* `for`

### Estruturas de dados

* Listas
* Dicionários
* Dicionários aninhados
* `enumerate()`
* `any()`

### Funções

* Parâmetros
* Retorno de múltiplos valores
* Argumentos posicionais
* Argumentos nomeados
* Parâmetros somente posicionais
* Parâmetros somente nomeados

### Validação e tratamento

* `try / except`
* `ValueError`
* Validação de entrada
* Validação de regras de negócio

### Arquivos e módulos

* `import`
* Módulos próprios
* `json`
* `pathlib.Path`
* Leitura e escrita de arquivos

### Datas

* `datetime.date`
* `date.today()`
* Criação de datas
* Comparação de datas

---

## 🔄 Fluxo da Aplicação

O funcionamento geral pode ser representado da seguinte forma:

```text
                    ┌───────────────┐
                    │    main.py    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Iniciar Caixa │
                    └───────┬───────┘
                            │
                       CPF do usuário
                            │
                    ┌───────▼───────┐
                    │    Usuário    │
                    └───────┬───────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
             Encontrado             Novo usuário
                 │                     │
                 │              Cadastro + JSON
                 │                     │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │  Conta Corrente     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Caixa Eletrônico   │
                 └──────────┬──────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
      Depositar           Sacar            Extrato
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                       Atualiza JSON
```

---

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/raffindev/dio.git
```

Entre no diretório do desafio:

```bash
cd "Vivo - Python AI Backend Developer/02_desafio_cx_eletronico.py"
```

Execute:

```bash
python main.py
```

> É necessário ter o **Python 3** instalado.

---

## 📌 Status

🟢 **Concluído**

O desafio foi desenvolvido como parte da formação **Vivo — Python AI Backend Developer**.

---