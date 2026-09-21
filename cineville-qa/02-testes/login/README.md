# Testes de Autenticação e Recuperação de Acesso

## Objetivo

Validar os principais fluxos de autenticação e recuperação de acesso da aplicação Cineville, considerando cenários positivos, negativos, validações de regras de negócio, testes de API, testes de Front-end e automação.

Este projeto foi desenvolvido como parte da experiência prática em QA, envolvendo desde o entendimento das regras de negócio e elaboração dos casos de teste até a execução e documentação dos testes.

---

## Escopo

O escopo deste projeto contempla os seguintes fluxos:

### 1. Login

Validação do processo de autenticação do usuário, incluindo:

- Login com credenciais válidas
- Login de usuário comum
- Login de administrador
- E-mail inválido
- Senha inválida
- Campos obrigatórios
- Controle de tentativas de login
- Tratamento de excesso de requisições

### 2. Recuperação de senha

Validação do fluxo de recuperação de acesso:

- E-mail válido
- E-mail não cadastrado
- E-mail não informado
- Solicitação de recuperação de senha
- Tratamento das respostas da API

### 3. Redefinição de senha

Validação do processo de redefinição:

- Token válido
- Token inválido
- Token vazio
- Token expirado
- Nova senha vazia
- Confirmação de senha vazia
- Senhas diferentes
- Senha fora do padrão
- Nova senha igual à senha anterior
- Excesso de requisições
- Requisição sem body

---

## Fluxo funcional

```text
Login
  ↓
Esqueceu a senha?
  ↓
Recuperação de senha
  ↓
Redefinição de senha
  ↓
Novo login

