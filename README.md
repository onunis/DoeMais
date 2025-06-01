# DoeMais 🕊️

**DoeMais** é uma aplicação desenvolvida em Python com interface gráfica feita em `Tkinter` e a utilização de `CRUD` para a manipulação de dados. Seu objetivo é gerenciar e registrar doações feitas por usuários, facilitando o controle e visualização dos dados de doação. O projeto foca em acessibilidade e praticidade, sendo ideal para organizações sociais, ONGs ou projetos de caridade.

---

## 📌 Funcionalidades

- Tela de **login** com autenticação simples.
- Registro de **doações** com informações como:
  - Nome do doador
  - Tipo da doação (alimentos, roupas, etc.)
  - Quantidade
  - Data
- Página principal com navegação entre seções.
- Armazenamento local das informações em um banco de dados SQLite (`doacoes.db`).
- Organização de código em módulos e reutilização de componentes.

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.11+**
- **Tkinter** — Interface gráfica
- **SQLite** — Banco de dados leve e local

---

## 🗂️ Estrutura de Pastas

DoeMais-main/
│
├── main.py # Ponto de entrada da aplicação
├── login.py # Tela de login
├── principal.py # Tela principal com menus
├── banco.py # Gerenciamento do banco de dados
├── doacoes.db # Arquivo do banco SQLite
├── paginas/
│ ├── formulario.py # Formulário de cadastro de doações
│ └── doacoes.py # Tela de visualização das doações
└── pycache/ # Cache gerado automaticamente


---

## ▶️ Como Executar

1. **Pré-requisitos:**
   - Python 3.11 instalado no sistema.

2. **Clone ou extraia o projeto:**
   ```bash
   git clone https://github.com/onunis/DoeMais.git
   # ou
   unzip DoeMais-main.zip


## 🔐 Login
O sistema utiliza uma verificação básica de login (sem senha por padrão, mas o código permite implementar autenticação com mais segurança, se necessário).

## 🧠 Lógica do Sistema
A execução inicia por main.py, que chama a tela de login.

Após o login, o usuário é redirecionado à principal.py, onde há navegação para:

formulario.py – onde são cadastradas novas doações.

doacoes.py – onde é possível consultar as doações já registradas.

O módulo banco.py centraliza a lógica de acesso e manipulação do banco de dados SQLite.

## 🎯 Objetivo Acadêmico
Este projeto foi desenvolvido como parte de um trabalho acadêmico com o objetivo de aplicar conceitos de:

Programação orientada a objetos

Interfaces gráficas com Tkinter

Persistência de dados com SQLite

Modularização de código e boas práticas de organização

## 📸 Capturas de Tela
'''Inserir'''

## 👨‍💻 Autores
Nome: Guilherme de Araújo Nunes, Larissa Gabriel dos Santos e Gabriel Alves Campos

Curso: Análise e Desenvolvimento de Sistemas

Disciplina: Desenvolvimento Rápido de Aplicações em Python 2025.1

## 📄 Licença
Este projeto é de cunho acadêmico e livre para aprendizado.
