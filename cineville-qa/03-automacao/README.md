# 🤖 Automação de Testes - Cineville

## 📌 Sobre o projeto

Este diretório apresenta a automação de testes desenvolvida para o projeto Cineville, utilizando Robot Framework.

A automação foi criada como parte da experiência prática em QA, com foco na validação de fluxos de API e aplicação web, utilização de dados dinâmicos, organização de recursos reutilizáveis e execução automatizada dos testes.

O projeto também demonstra conceitos importantes de automação, como:

- criação de dados para teste;
- execução de testes de API;
- validação de respostas HTTP;
- validação de estruturas JSON;
- utilização de variáveis de ambiente;
- reutilização de keywords;
- Setup e Teardown;
- limpeza dos dados utilizados nos testes;
- organização de testes por suíte;
- preparação para execução em CI/CD.

---

# 🎯 Objetivo

Automatizar cenários de teste relacionados ao sistema Cineville, reduzindo a execução manual de testes repetitivos e permitindo validar os principais comportamentos da aplicação de forma automatizada.

O foco inicial da automação foi o fluxo de autenticação, utilizando uma abordagem que permite criar um usuário de teste, realizar o login e posteriormente remover o usuário utilizado durante a execução.

---

# 🧪 Abordagem de testes

A automação utiliza uma estrutura baseada em **BDD (Behavior Driven Development)**, organizando os testes de maneira próxima ao comportamento esperado do sistema.

A estrutura busca representar:

```text
Dado que existe um usuário de teste
        ↓
Quando o usuário realiza o login
        ↓
Então o sistema deve autenticar o usuário
        ↓
E retornar um token de autenticação
        ↓
Ao final, o usuário de teste é removido
