# Sistema de Gerenciamento de Loja de Roupas

Este é um sistema desenvolvido em Python para o gerenciamento de uma loja de roupas, com funcionalidades de cadastro de clientes, vendedores, produtos e vendas. O sistema também permite a geração de relatórios de vendas por cliente, período e vendedor.

## Funcionalidades

- **Cadastro de Clientes:** Inclui informações como CPF, nome, data de nascimento, categoria do cliente e endereço.
- **Cadastro de Vendedores:** Contém dados como CPF, nome, data de nascimento, código de vendedor e data de contratação.
- **Cadastro de Produtos:** Registra o código do produto, nome, descrição, tamanho, cor e preço.
- **Registro de Vendas:** Registra as vendas realizadas, associando clientes, vendedores e produtos vendidos, com a data e o valor total da venda.
- **Relatórios de Vendas:** Gera relatórios de vendas detalhados por cliente, vendedor ou período.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Paradigma:** Programação Orientada a Objetos
- **Arquitetura:** MVC

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Felipe041198/ClothingStore.git
   ```

2. Instale o Python.

3. Execute o sistema:

    Navegue até o diretório principal e execute o arquivo principal do sistema.
    ```bash
    python main.py
    ```

## Ferramentas de lint

### Flake8

   Este projeto segue o guia de estilo PEP 8 para Python. Para garantir que o código siga as melhores práticas de programação, utilizamos a ferramenta **Flake8** para validar o estilo do código.

### Configuração do Flake8

1. **Instalação do Flake8:**

   No seu computador, instale o Flake8 executando o seguinte comando:

   ```bash
   pip install flake8
   ```
   
2. **Executar o Flake8:**
   
   Você deve executar na pasta raiz do projeto o comando:

   ```bash
   flake8
   ```
3. **Configurar o Flake8:**

   Na raiz do projeto existe um arquivo de configuração do flake8 chamado [`.flake8`](./.flake8). Esse arquivo é responsável por definir as configurações do Flake.
   Como por exemplo o número máximo de caracteres ou quais regras do PEP 8 podemos ignorar.

## Estrutura do projeto

//TODO