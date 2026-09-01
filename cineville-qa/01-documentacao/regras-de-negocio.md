# 📋 Regras de Negócio — Cineville

Este documento apresenta as principais regras de negócio utilizadas
como base para os testes das funcionalidades do projeto Cineville.

---

# 🔐 1. Tela de Login

## Descrição

A tela de login deverá ser o ponto de entrada do sistema para
usuários já cadastrados.

A autenticação será realizada por meio de e-mail e senha, permitindo
acesso às funcionalidades autorizadas conforme o perfil do usuário.

Após autenticação bem-sucedida, o sistema deverá criar uma sessão
autenticada e redirecionar o usuário para a página inicial
correspondente ao seu perfil.

A tela também deverá permitir acesso ao fluxo de recuperação de
senha e ao cadastro de novos usuários.

---

## 👤 História de Usuário

**Como** Product Owner (PO)

**Quero** que seja desenvolvida uma tela de login para autenticação
dos usuários da plataforma

**Para** que clientes, funcionários, gerentes e administradores
possam acessar suas funcionalidades de forma segura, conforme
seu perfil de acesso.

---

# ✅ 2. Critérios de Aceite

A tela de Login deve conter:

- Botão **Criar conta**
- Botão **Fazer login**
- Botão **Entrar com a conta Google**
- Campo de texto **E-mail**
- Campo de texto **Senha**
- Botão **Entrar**
- Link **Esqueceu sua senha?**
- Mensagem **Não possui uma conta?**
- Link **Criar conta**
- Botão **Suporte**

---

# 📋 3. Regras de Negócio

## RN-LOGIN-001 — Criar conta

A tela deve conter um botão **Criar conta**.

### Comportamento esperado

Ao clicar no botão **Criar conta**, o usuário deverá ser
direcionado para a tela de criação de conta.

---

## RN-LOGIN-002 — Fazer login

A tela deve conter um botão **Fazer login**.

### Comportamento esperado

Ao clicar no botão **Fazer login**, deverá ser aberta a tela
de login.

---

## RN-LOGIN-003 — Login com conta Google

A tela deve conter um botão **Entrar com a conta Google**.

### Comportamento esperado

Ao clicar no botão **Entrar com a conta Google**, deverá ser
aberta uma tela para escolha da conta Google.

Ao selecionar a conta, os dados deverão ser inseridos
automaticamente.

---

## RN-LOGIN-004 — Campo E-mail

A tela deve conter um campo de texto para e-mail.

### Regras

- O campo e-mail é obrigatório.
- O campo deve conter um placeholder.
- O e-mail deve possuir formato válido.
- Formatos esperados:
  - nome@dominio.com
  - nome@dominio.com.br

---

## RN-LOGIN-005 — Campo Senha

A tela deve conter um campo de texto para senha.

### Regras

- O campo senha é obrigatório.
- O campo deve conter um placeholder.
- Deve existir uma opção para mostrar ou ocultar a senha,
  representada pelo ícone de olho.

---

## RN-LOGIN-006 — Autenticação

A tela deve conter um botão **Entrar**.

### Comportamento esperado

Caso algum dos campos seja divergente dos dados existentes
na base de dados, o sistema deverá retornar a mensagem:

> **E-mail e/ou senha inválidos.**

Quando todos os campos estiverem preenchidos corretamente,
deverá ser possível acessar a biblioteca.

---

## RN-LOGIN-007 — Recuperação de senha

A tela deve conter o link:

**Esqueceu sua senha?**

### Comportamento esperado

Ao clicar no link, o usuário deverá ser direcionado para a
tela de recuperação de senha.

---

## RN-LOGIN-008 — Criação de conta

A tela deve apresentar a mensagem:

**Não possui uma conta?**

Também deverá apresentar o link:

**Criar conta**

### Comportamento esperado

Ao clicar no link **Criar conta**, o usuário deverá ser
direcionado para a tela de criação de conta.

---

## RN-LOGIN-009 — Campos não clicáveis

Os campos destacados em amarelo não serão clicáveis.

---

# 🧪 4. Aplicação das regras nos testes

As regras de negócio da tela de Login servem como base para
a elaboração dos cenários de teste.

A partir dessas regras podem ser realizados:

- Testes funcionais
- Testes positivos
- Testes negativos
- Testes de validação de campos
- Testes de autenticação
- Testes de navegação
- Testes de mensagens
- Testes de API
- Testes automatizados

---

# 🔗 5. Relação com os testes

As regras documentadas nesta seção serão relacionadas aos
casos de teste e às evidências de execução do projeto.

Exemplo:

| Regra | Cenário | Tipo |
|---|---|---|
| RN-LOGIN-004 | E-mail válido | Positivo |
| RN-LOGIN-004 | E-mail inválido | Negativo |
| RN-LOGIN-004 | E-mail vazio | Negativo |
| RN-LOGIN-005 | Senha válida | Positivo |
| RN-LOGIN-005 | Senha vazia | Negativo |
| RN-LOGIN-006 | Credenciais válidas | Positivo |
| RN-LOGIN-006 | Credenciais inválidas | Negativo |
| RN-LOGIN-007 | Acessar recuperação de senha | Navegação |
| RN-LOGIN-008 | Acessar criação de conta | Navegação |
