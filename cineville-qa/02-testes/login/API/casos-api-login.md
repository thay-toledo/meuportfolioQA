# Casos de Teste - API Login

## Objetivo

Validar o funcionamento da API de autenticação,
garantindo que o login responda corretamente para
credenciais válidas e inválidas.

## Endpoint

`POST /api/auth/login`

## Casos de teste

### CT-API-LOGIN-001
Login com e-mail e senha válidos.

**Esperado:** HTTP 200 e autenticação realizada com sucesso.

### CT-API-LOGIN-002
Login com senha inválida.

**Esperado:** HTTP 401.

**Mensagem esperada:**

`E-mail ou senha incorretos.`

### CT-API-LOGIN-003
Login com e-mail inválido.

**Esperado:** HTTP 401.

### CT-API-LOGIN-004
Login sem informar e-mail.

**Esperado:** HTTP 400.

### CT-API-LOGIN-005
Login sem informar senha.

**Esperado:** HTTP 400.

### CT-API-LOGIN-006
Login sem informar e-mail e senha.

**Esperado:** HTTP 400.

### CT-API-LOGIN-007
Excesso de tentativas de login.

**Esperado:** HTTP 429.

**Mensagem esperada:**

`ThrottlerException: Too Many Requests`
