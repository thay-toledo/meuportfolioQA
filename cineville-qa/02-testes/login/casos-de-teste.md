# Casos de Teste - Login

## Objetivo

Validar o funcionamento da tela de login, garantindo que o usuário consiga
acessar o sistema com credenciais válidas e que o sistema apresente as
mensagens corretas para dados inválidos ou campos não preenchidos.

---

## CT-LOGIN-001 - Login com credenciais válidas

**Objetivo:**  
Validar o acesso ao sistema utilizando e-mail e senha válidos.

**Pré-condições:**
- Usuário cadastrado no sistema.
- Usuário possuir e-mail e senha válidos.
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Informar um e-mail válido.
3. Informar uma senha válida.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema deve autenticar o usuário.
- O usuário deve ser direcionado para a página inicial.
- O acesso deve ser realizado com sucesso.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-002 - Login com e-mail inválido

**Objetivo:**  
Validar o comportamento do sistema ao informar um e-mail inválido.

**Pré-condições:**
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Informar um e-mail inválido.
3. Informar uma senha válida.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar a mensagem:

> E-mail ou senha incorretos.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-003 - Login com senha inválida

**Objetivo:**  
Validar o comportamento do sistema ao informar uma senha inválida.

**Pré-condições:**
- Usuário cadastrado no sistema.
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Informar um e-mail válido.
3. Informar uma senha inválida.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar a mensagem:

> E-mail ou senha incorretos.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-004 - Login com e-mail e senha inválidos

**Objetivo:**  
Validar o comportamento do sistema quando e-mail e senha são inválidos.

**Pré-condições:**
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Informar um e-mail inválido.
3. Informar uma senha inválida.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar a mensagem:

> E-mail ou senha incorretos.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-005 - Login sem preencher os campos

**Objetivo:**  
Validar o comportamento do sistema quando o usuário tenta realizar o login
sem preencher e-mail e senha.

**Pré-condições:**
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Não preencher o campo de e-mail.
3. Não preencher o campo de senha.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar as mensagens de validação dos campos obrigatórios.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-006 - Login com e-mail válido e senha vazia

**Objetivo:**  
Validar a obrigatoriedade do campo senha.

**Pré-condições:**
- Usuário cadastrado no sistema.
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Informar um e-mail válido.
3. Não preencher a senha.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar a validação referente ao campo senha obrigatório.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-007 - Login com e-mail vazio e senha válida

**Objetivo:**  
Validar a obrigatoriedade do campo e-mail.

**Pré-condições:**
- Sistema estar disponível.

**Passos:**
1. Acessar a tela de login.
2. Não preencher o campo de e-mail.
3. Informar uma senha válida.
4. Clicar no botão **ENTRAR**.

**Resultado esperado:**
- O sistema não deve realizar o login.
- Deve apresentar a validação referente ao campo e-mail obrigatório.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-008 - Acessar recuperação de senha

**Objetivo:**  
Validar o acesso à funcionalidade de recuperação de senha.

**Pré-condições:**
- Usuário estar na tela de login.

**Passos:**
1. Acessar a tela de login.
2. Clicar no link **Esqueceu a senha?**

**Resultado esperado:**
- O usuário deve ser direcionado para a tela de recuperação de senha.
- A URL esperada deve ser:

`/forgot-password`

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

## CT-LOGIN-009 - Validar botão de login

**Objetivo:**  
Validar a identificação e funcionamento do botão de login.

**Pré-condições:**
- Usuário estar na tela de login.

**Passos:**
1. Acessar a tela de login.
2. Localizar o botão de login.

**Resultado esperado:**
- O botão deve estar identificado como **ENTRAR**.
- O botão deve estar disponível para interação.

**Resultado obtido:**  
A preencher durante a execução.

**Status:**  
A executar.

---

# Resumo dos casos

| ID | Cenário | Tipo | Status |
|---|---|---|---|
| CT-LOGIN-001 | Login com credenciais válidas | Positivo | A executar |
| CT-LOGIN-002 | E-mail inválido | Negativo | A executar |
| CT-LOGIN-003 | Senha inválida | Negativo | A executar |
| CT-LOGIN-004 | E-mail e senha inválidos | Negativo | A executar |
| CT-LOGIN-005 | Campos vazios | Negativo | A executar |
| CT-LOGIN-006 | Senha vazia | Negativo | A executar |
| CT-LOGIN-007 | E-mail vazio | Negativo | A executar |
| CT-LOGIN-008 | Recuperação de senha | Funcional | A executar |
| CT-LOGIN-009 | Validação do botão ENTRAR | Interface | A executar |
