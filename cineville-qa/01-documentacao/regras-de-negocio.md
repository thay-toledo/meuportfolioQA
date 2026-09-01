# 🔐 1. Tela de Login

## 1.1 Descrição

A tela de login deverá ser o ponto de entrada do sistema para
usuários já cadastrados.

A autenticação será realizada por meio de e-mail e senha,
permitindo acesso às funcionalidades autorizadas conforme
o perfil do usuário.

Após autenticação bem-sucedida, o sistema deverá criar uma
sessão autenticada e redirecionar o usuário para a página
inicial correspondente ao seu perfil.

A tela também deverá permitir acesso ao fluxo de recuperação
de senha e ao cadastro de novos usuários.

---

## 1.2 História de Usuário

**Como** Product Owner (PO)

**Quero** que seja desenvolvida uma tela de login para
autenticação dos usuários da plataforma

**Para** que clientes, funcionários, gerentes e administradores
possam acessar suas funcionalidades de forma segura, conforme
seu perfil de acesso.

---

# 🔑 2. Fluxo de Autenticação

O fluxo de login é responsável por autenticar os usuários
cadastrados na plataforma por meio de suas credenciais.

Após a autenticação, o sistema deve emitir um token de acesso
para utilização nas rotas protegidas.

## 2.1 Processo de autenticação

1. O usuário envia suas credenciais de acesso:
   `email` e `password`.

2. O sistema valida as credenciais contra o banco de dados.

3. Quando as credenciais estão corretas, o sistema executa
   a função interna `generateToken`.

4. A função gera um token JWT (JSON Web Token).

5. O token é retornado na resposta da autenticação.

6. O token deve ser utilizado nas requisições subsequentes
   para acesso às rotas protegidas.

---

# 🛡️ 3. Rate Limiting

Para reduzir o risco de ataques de força bruta (*brute-force*)
e contribuir para a disponibilidade do serviço, foi definida
uma política de limite de requisições para o endpoint de Login.

## RN-LOGIN-010 — Limite de tentativas

Cada usuário, rastreado por IP/identificador, pode realizar
no máximo:

**5 tentativas de login a cada 1 minuto.**

### Comportamento esperado

Quando o limite de 5 requisições for excedido dentro da janela
de 60 segundos, o servidor deve recusar as tentativas adicionais.

### Retorno esperado

```text
HTTP 429 — Too Many Requests
