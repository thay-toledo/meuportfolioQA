# Casos de Teste - Autenticação e Recuperação de Acesso

## Objetivo

Validar os principais fluxos de autenticação e recuperação de acesso da aplicação Cineville, verificando o comportamento do sistema em cenários positivos, negativos e de limite.

---

# 1. Casos de Teste - Login

## CT-LOGIN-001 - Login com sucesso - usuário comum

**Objetivo:**

Validar o acesso ao sistema utilizando credenciais válidas de um usuário comum.

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
- O usuário deve ter acesso ao sistema.

**Resultado obtido:**

Login realizado com sucesso.

**Status:**

✅ Passou

---

## CT-LOGIN-002 - Login com sucesso - administrador

**Objetivo:**

Validar o acesso ao sistema utilizando credenciais válidas de um usuário administrador.

**Pré-condições:**

- Usuário administrador cadastrado.
- Credenciais válidas.
- Sistema disponível.

**Passos:**

1. Acessar a tela de login.
2. Informar o e-mail do administrador.
3. Informar a senha válida.
4. Clicar em **ENTRAR**.

**Resultado esperado:**

- O administrador deve ser autenticado.
- O acesso deve ser concedido conforme o perfil do usuário.

**Resultado obtido:**

Login de administrador realizado com sucesso.

**Status:**

✅ Passou

---

## CT-LOGIN-003 - Login com e-mail inválido

**Objetivo:**

Validar o comportamento do sistema ao informar um e-mail inválido.

**Passos:**

1. Acessar a tela de login.
2. Informar um e-mail inválido.
3. Informar uma senha válida.
4. Clicar em **ENTRAR**.

**Resultado esperado:**

- O sistema não deve realizar o login.
- Deve apresentar a mensagem de erro definida para credenciais inválidas.

**Resultado obtido:**

Sistema rejeitou a autenticação e apresentou a mensagem esperada.

**Status:**

✅ Passou

---

## CT-LOGIN-004 - Login com senha inválida

**Objetivo:**

Validar o comportamento do sistema ao informar uma senha inválida.

**Passos:**

1. Acessar a tela de login.
2. Informar um e-mail válido.
3. Informar uma senha inválida.
4. Clicar em **ENTRAR**.

**Resultado esperado:**

- O sistema não deve realizar o login.
- Deve apresentar a mensagem de erro definida para credenciais inválidas.

**Resultado obtido:**

Sistema rejeitou a autenticação e apresentou a mensagem esperada.

**Status:**

✅ Passou

---

## CT-LOGIN-005 - Campos obrigatórios

**Objetivo:**

Validar a obrigatoriedade dos campos de e-mail e senha.

**Passos:**

1. Acessar a tela de login.
2. Deixar o campo e-mail vazio.
3. Deixar o campo senha vazio.
4. Clicar em **ENTRAR**.

**Resultado esperado:**

- O sistema não deve realizar o login.
- Os campos obrigatórios devem ser validados.

**Resultado obtido:**

Campos obrigatórios validados conforme esperado.

**Status:**

✅ Passou

---

## CT-LOGIN-006 - Limite de tentativas de login

**Objetivo:**

Validar o comportamento da aplicação após múltiplas tentativas de autenticação.

**Passos:**

1. Realizar tentativas consecutivas de login.
2. Repetir a requisição até atingir o limite definido.
3. Realizar uma nova tentativa após atingir o limite.

**Resultado esperado:**

- O sistema deve controlar o número de tentativas.
- Ao exceder o limite, a API deve retornar o status correspondente ao bloqueio por excesso de requisições.

**Resultado obtido:**

Regra de limite de tentativas validada.

**Status:**

✅ Passou

---

# 2. Casos de Teste - Recuperação de Senha

## CT-REC-001 - Recuperação com e-mail válido

**Objetivo:**

Validar a solicitação de recuperação de senha utilizando um e-mail cadastrado.

**Passos:**

1. Acessar a opção **Esqueceu sua senha?**
2. Informar um e-mail cadastrado.
3. Solicitar o link de recuperação.

**Resultado esperado:**

- A solicitação deve ser processada.
- O sistema deve informar o envio do link de recuperação.

**Resultado obtido:**

Mensagem de link enviado apresentada conforme esperado.

**Status:**

✅ Passou

---

## CT-REC-002 - Recuperação com e-mail não cadastrado

**Objetivo:**

Validar o comportamento da recuperação utilizando um e-mail não cadastrado.

**Passos:**

1. Acessar a recuperação de senha.
2. Informar um e-mail não cadastrado.
3. Solicitar a recuperação.

**Resultado esperado:**

- O sistema deve apresentar o comportamento definido para e-mail não cadastrado.
- Não deve realizar uma recuperação para um usuário inexistente.

**Resultado obtido:**

Sistema apresentou a mensagem esperada para e-mail não cadastrado.

**Status:**

✅ Passou

---

## CT-REC-003 - Recuperação com e-mail vazio

**Objetivo:**

Validar a obrigatoriedade do campo e-mail.

**Passos:**

1. Acessar a recuperação de senha.
2. Não preencher o campo e-mail.
3. Solicitar a recuperação.

**Resultado esperado:**

- O sistema não deve processar a solicitação.
- Deve apresentar a validação do campo obrigatório.

**Resultado obtido:**

Campo e-mail validado conforme esperado.

**Status:**

✅ Passou

---

# 3. Casos de Teste - Redefinição de Senha

## CT-RESET-001 - Token válido

Validar a utilização de um token válido para redefinição de senha.

**Status:** ✅ Passou

---

## CT-RESET-002 - Token inválido

Validar a rejeição de um token inválido.

**Status:** ✅ Passou

---

## CT-RESET-003 - Token vazio

Validar a obrigatoriedade do token de recuperação.

**Status:** ✅ Passou

---

## CT-RESET-004 - Token expirado

Validar a rejeição de um token expirado.

**Cenário executado:** token com 5 horas.

**Status:** ✅ Passou

---

## CT-RESET-005 - Nova senha vazia

Validar a obrigatoriedade do campo de nova senha.

**Status:** ✅ Passou

---

## CT-RESET-006 - Confirmação de senha vazia

Validar a obrigatoriedade da confirmação da nova senha.

**Status:** ✅ Passou

---

## CT-RESET-007 - Senhas diferentes

Validar o comportamento quando a confirmação da senha não corresponde à nova senha.

**Status:** ✅ Passou

---

## CT-RESET-008 - Senha fora do padrão

Validar as regras de complexidade definidas para a nova senha.

**Status:** ✅ Passou

---

## CT-RESET-009 - Nova senha diferente da anterior

Validar a alteração da senha utilizando uma nova senha diferente da anterior.

**Status:** ✅ Passou

---

## CT-RESET-010 - HTTP 429

Validar o comportamento da API diante do excesso de requisições.

**Status:** ✅ Passou

---

## CT-RESET-011 - Excesso de validações

Validar o comportamento da aplicação diante de múltiplas tentativas de validação.

**Status:** ✅ Passou

---

## CT-RESET-012 - Login após redefinição de senha

Validar a autenticação utilizando a senha após o processo de redefinição.

**Cenário executado:** 5 tentativas de login.

**Status:** ✅ Passou

---

## CT-RESET-013 - Requisição sem body

Validar o comportamento da API quando uma requisição é enviada sem corpo.

**Status:** ✅ Passou

---

# Resumo dos Casos

| ID | Cenário | Tipo | Status |
|---|---|---|---|
| CT-LOGIN-001 | Login - usuário comum | Positivo | ✅ Passou |
| CT-LOGIN-002 | Login - administrador | Positivo | ✅ Passou |
| CT-LOGIN-003 | E-mail inválido | Negativo | ✅ Passou |
| CT-LOGIN-004 | Senha inválida | Negativo | ✅ Passou |
| CT-LOGIN-005 | Campos obrigatórios | Negativo | ✅ Passou |
| CT-LOGIN-006 | Limite de tentativas | Limite | ✅ Passou |
| CT-REC-001 | E-mail válido | Positivo | ✅ Passou |
| CT-REC-002 | E-mail não cadastrado | Negativo | ✅ Passou |
| CT-REC-003 | E-mail vazio | Negativo | ✅ Passou |
| CT-RESET-001 | Token válido | Positivo | ✅ Passou |
| CT-RESET-002 | Token inválido | Negativo | ✅ Passou |
| CT-RESET-003 | Token vazio | Negativo | ✅ Passou |
| CT-RESET-004 | Token expirado | Negativo | ✅ Passou |
| CT-RESET-005 | Nova senha vazia | Negativo | ✅ Passou |
| CT-RESET-006 | Confirmação vazia | Negativo | ✅ Passou |
| CT-RESET-007 | Senhas diferentes | Negativo | ✅ Passou |
| CT-RESET-008 | Senha fora do padrão | Negativo | ✅ Passou |
| CT-RESET-009 | Nova senha diferente da anterior | Positivo | ✅ Passou |
| CT-RESET-010 | HTTP 429 | Limite | ✅ Passou |
| CT-RESET-011 | Excesso de validações | Limite | ✅ Passou |
| CT-RESET-012 | Login após redefinição | Integração | ✅ Passou |
| CT-RESET-013 | Requisição sem body | Negativo | ✅ Passou |
