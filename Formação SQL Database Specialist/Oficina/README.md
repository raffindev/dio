# Projeto Oficina Mecânica

Projeto desenvolvido durante a Formação SQL Database Specialist, da DIO, com foco na modelagem de um banco de dados relacional para um sistema de controle e gerenciamento de ordens de serviço em uma oficina mecânica.

## 🎯 Objetivo

Construir um modelo de banco de dados capaz de representar o processo de execução de ordens de serviço em uma oficina mecânica, aplicando conceitos de:

* Modelagem de dados;
* Modelo Entidade-Relacionamento Estendido (EER);
* Chaves primárias e estrangeiras;
* Cardinalidades;
* Relacionamentos 1:1, 1:N e N:N;
* Tabelas associativas;
* Especialização de entidades;
* Restrições de integridade.

## 🗄️ Modelo

O modelo contempla entidades relacionadas a:

* Pessoas;
* Clientes;
* Mecânicos;
* Equipes;
* Veículos;
* Ordens de Serviço;
* Serviços;
* Mão de Obra;
* Peças.

O modelo foi construído e refinado a partir da narrativa proposta no desafio, buscando representar as regras de negócio de forma consistente.

### Decisões de modelagem

* A entidade `Pessoa` foi utilizada como entidade base para `Cliente` e `Mecânico`, evitando a duplicação de informações comuns.
* `CPF` foi adicionado à entidade `Cliente` como identificador único.
* `RENAVAM` foi adicionado à entidade `Veículo` como identificador único.
* A entidade `Serviços` foi utilizada como tabela associativa entre `Ordem de Serviço` e `Tabela de Mão de Obra`, permitindo que uma OS possua vários serviços.
* Foi considerado que uma OS possui pelo menos um serviço e uma ou mais peças.
* Foi considerado que cada peça pertence a uma única Ordem de Serviço.
* O atributo `autorizado` foi adicionado à Ordem de Serviço para representar a autorização do cliente para execução dos serviços.
* `data_entrega` e `data_conclusao` foram consideradas informações distintas: a primeira representa a data prevista para entrega e a segunda a conclusão efetiva dos trabalhos.
* A entidade `Fornecedor` não foi incluída, pois o desafio não especifica controle de fornecedores, compras ou estoque de peças.

## 🛠️ Ferramenta

* MySQL Workbench

## 📁 Arquivos

* `oficina.mwb` — modelo desenvolvido no MySQL Workbench.
* `oficina.png` — representação visual do modelo final.
