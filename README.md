# 📦 Sistema de Estoque

Sistema de gerenciamento de estoque desenvolvido em **Python**, com persistência de dados utilizando **SQLite** e **SQLAlchemy**.

O projeto foi desenvolvido para praticar conceitos de **Programação Orientada a Objetos (POO)**, operações CRUD, persistência de dados e organização de código.

> **Status:** V1.0 — Projeto finalizado para fins de estudo e portfólio.

---

## 🖥️ Sobre o projeto

O Sistema de Estoque permite realizar operações básicas de gerenciamento de produtos através do terminal.

### Funcionalidades

* ➕ Cadastrar produtos
* 📋 Listar produtos
* 🔎 Buscar produtos pelo SKU
* ✏️ Atualizar produtos
* 🗑️ Remover produtos
* 💾 Persistir dados em banco SQLite

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python 3
* 🗄️ SQLite
* 🔗 SQLAlchemy
* 🌱 Git
* 🐙 GitHub

---

## 🏗️ Estrutura do projeto

```text
sistema-estoque/
│
├── models/
│   └── produto.py
│
├── services/
│   └── estoque_service.py
│
├── database/
│   ├── connection.py
│   └── produto_repository.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Organização

**`models/`**

Contém os modelos utilizados pela aplicação.

**`services/`**

Responsável pelas operações relacionadas ao gerenciamento do estoque.

**`database/`**

Responsável pela conexão com o banco de dados e pela persistência dos produtos.

**`main.py`**

Ponto de entrada da aplicação e responsável pela interação com o usuário através do terminal.

**`requirements.txt`**

Contém as dependências necessárias para executar o projeto.

---

## ⚙️ Funcionalidades

### ➕ Adicionar produto

Permite cadastrar um produto informando:

* Nome
* SKU
* Preço
* Quantidade

### 📋 Listar produtos

Exibe todos os produtos cadastrados no banco de dados.

### 🔎 Buscar produto

Realiza a busca de um produto através do seu SKU.

### ✏️ Atualizar produto

Permite alterar:

* Nome
* Preço
* Quantidade

O SKU é utilizado para localizar o produto.

### 🗑️ Remover produto

Permite excluir um produto através do SKU, solicitando confirmação antes da remoção.

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/medeirosalves/sistema-estoque.git
```

### 2. Acesse a pasta do projeto

```bash
cd sistema-estoque
```

### 3. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

### 4. Ative o ambiente virtual

Linux:

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
python main.py
```

---

## 💾 Banco de dados

A aplicação utiliza **SQLite** como banco de dados.

O SQLAlchemy é utilizado como ORM para facilitar a comunicação entre a aplicação Python e o banco de dados.

As tabelas necessárias são criadas automaticamente quando a aplicação é executada.

---

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados:

* Programação Orientada a Objetos
* Classes e objetos
* CRUD
* ORM
* SQLAlchemy
* SQLite
* Persistência de dados
* Gerenciamento de sessões
* Separação de responsabilidades
* Organização de projetos Python
* Git e GitHub

---

## 🎯 Objetivo

Este projeto foi desenvolvido como parte dos meus estudos em **Python e desenvolvimento de software**, buscando transformar conceitos teóricos em uma aplicação funcional.

A versão atual representa uma etapa prática do meu aprendizado, principalmente em relação a **POO, banco de dados, SQLAlchemy e organização de projetos**.

---

## 📌 Status do projeto

**V1.0 — Finalizado**

O projeto será mantido nesta versão como um projeto de estudo e portfólio.

Novas funcionalidades e tecnologias serão exploradas em projetos futuros.

---

## 👨‍💻 Autor

**Luan Medeiros**

Desenvolvedor Python em formação, com interesse em desenvolvimento de software, automação e cibersegurança.
