# Casos de Teste - `Sauce Demo`

Este documento contém os casos de teste manuais criados para validar as principais funcionalidades da aplicação `Sauce Demo`.

## Resumo dos casos de teste

| ID | Funcionalidade | Cenário | Tipo | Prioridade | Status |
|---|---|---|---|---|---|
| CT-001 | Login | Login com usuário válido e senha válida | Positivo | Alta | A executar |
| CT-002 | Login | Login com usuário válido e senha inválida | Negativo | Alta | Aprovado |
| CT-003 | Login | Login com usuário inválido e senha válida | Negativo | Alta | Aprovado |
| CT-004 | Login | Login com campos vazios | Negativo | Alta | A executar |

---

## CT-001 - Login com usuário válido e senha válida

**Funcionalidade:** Login  
**Tipo de teste:** Positivo  
**Prioridade:** Alta  

### Objetivo

Validar se o sistema permite o acesso quando o usuário informa credenciais válidas.

### Pré-condições

- Acessar a aplicação `Sauce Demo`
- Estar na tela de login

### Massa de teste

| Campo | Valor |
|---|---|
| Usuário | standard_user |
| Senha | secret_sauce |

### Passos para execução

1. Acessar a página de login.
2. Preencher o campo usuário com `standard_user`.
3. Preencher o campo senha com `secret_sauce`.
4. Clicar no botão **Login**.

### Resultado esperado

O sistema deve permitir o login e redirecionar o usuário para a página de produtos.

### Resultado obtido

A definir após execução.

### Evidência

A definir.

### Status

A executar

---

## CT-002 - Login com usuário válido e senha inválida

**Funcionalidade:** Login  
**Tipo de teste:** Negativo  
**Prioridade:** Alta  

### Objetivo

Validar se o sistema impede o acesso quando o usuário informa um usuário válido, porém uma senha inválida.

### Pré-condições

- Acessar a aplicação `Sauce Demo`
- Estar na tela de login

### Massa de teste

| Campo | Valor |
|---|---|
| Usuário | standard_user |
| Senha | senha incorreta |

### Passos para execução

1. Acessar a página de login.
2. Preencher o campo usuário com `standard_user`.
3. Preencher o campo senha com uma senha inválida.
4. Clicar no botão **Login**.

### Resultado esperado

O sistema deve bloquear o acesso e exibir uma mensagem informando que as credenciais são inválidas.

### Resultado obtido

O sistema bloqueou o acesso e exibiu uma mensagem de erro informando que o nome de usuário e a senha não correspondem a nenhum usuário cadastrado.

### Evidência

Print da tela com mensagem de erro.

### Status

Aprovado

---

## CT-003 - Login com usuário inválido e senha válida

**Funcionalidade:** Login  
**Tipo de teste:** Negativo  
**Prioridade:** Alta  

### Objetivo

Validar se o sistema impede o acesso quando o usuário informa um nome de usuário inválido, mesmo utilizando uma senha válida.

### Pré-condições

- Acessar a aplicação `Sauce Demo`
- Estar na tela de login

### Massa de teste

| Campo | Valor |
|---|---|
| Usuário | standard_user121 |
| Senha | secret_sauce |

### Passos para execução

1. Acessar a página de login.
2. Preencher o campo usuário com `standard_user121`.
3. Preencher o campo senha com `secret_sauce`.
4. Clicar no botão **Login**.

### Resultado esperado

O sistema deve bloquear o acesso e exibir uma mensagem informando que as credenciais são inválidas.

### Resultado obtido

O sistema bloqueou o acesso e exibiu mensagem de erro informando que o nome de usuário e a senha não correspondem a nenhum usuário cadastrado.

### Evidência

Print da tela com mensagem de erro.

### Status

Aprovado

---

## CT-004 - Login com campos vazios

**Funcionalidade:** Login  
**Tipo de teste:** Negativo  
**Prioridade:** Alta  

### Objetivo

Validar se o sistema impede o login quando os campos obrigatórios de usuário e senha não são preenchidos.

### Pré-condições

- Acessar a aplicação `Sauce Demo`
- Estar na tela de login

### Massa de teste

| Campo | Valor |
|---|---|
| Usuário | vazio |
| Senha | vazio |

### Passos para execução

1. Acessar a página de login.
2. Deixar o campo usuário vazio.
3. Deixar o campo senha vazio.
4. Clicar no botão **Login**.

### Resultado esperado

O sistema deve bloquear o acesso e exibir uma mensagem informando que o campo usuário é obrigatório.

### Resultado obtido

A definir após execução.

### Evidência

A definir.

### Status

A executar
