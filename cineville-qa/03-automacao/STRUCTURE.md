# 📂 Estrutura do Projeto - Guia Detalhado

Este documento explica a organização de pastas e arquivos do template de automação, 
o papel de cada componente e como eles se relacionam.

---

## 🗂️ Visão Geral

```
projeto/
├── .github/
│   └── workflows/
│       └── pipeline.yml           → CI/CD (GitHub Actions)
├── fixtures/
│   ├── data.yaml.example          → Modelo de credenciais (seguro para commit)
│   ├── data.yaml                  → Credenciais reais (NÃO vai pro Git)
│   └── env.yaml                   → Configuração de ambientes (URLs)
├── pages/
│   └── pages_web.resource         → Page Objects (elementos da interface)
├── resources/
│   ├── keywords.resource          → Keywords globais (sessão, token, criações)
│   ├── users.resource             → Keywords do módulo Usuário
│   ├── company.resource           → Keywords do módulo Empresa
│   ├── board.resource             → Keywords do módulo Diretoria
│   ├── web.resource               → Keywords de interação Web (Selenium)
│   └── libs/
│       └── get_fake_person.py     → Gerador de dados fake (Python + Faker)
├── tests/
│   ├── api_tests/                 → Suítes de teste de API
│   │   ├── user.robot
│   │   ├── company.robot
│   │   └── board.robot
│   ├── web_tests/                 → Suítes de teste Web (Selenium)
│   │   ├── user.robot
│   │   └── company.robot
│   ├── get_config.py              → Parser de ambiente (--env)
│   └── run.py                     → Script auxiliar de execução
├── .gitignore                     → Regras de exclusão do Git
├── README.md                      → Documentação principal
├── STRUCTURE.md                   → Este arquivo (guia de estrutura)
└── requirements.txt               → Dependências Python do projeto
```

---

## 📋 Detalhamento por Camada

---

### 🔧 `.github/workflows/` — Pipeline de CI/CD

| Arquivo | Descrição |
|---------|-----------|
| `pipeline.yml` | Configuração do GitHub Actions |

**O que faz:**
- É acionado automaticamente em push ou Pull Request na branch `main`
- Instala Python 3.12 e as dependências do `requirements.txt`
- Executa todos os testes (API + Web)
- Salva os relatórios como artefatos
- Publica o relatório no GitHub Pages

**Quando editar:**
- Para adicionar notificações (Slack, email)
- Para mudar a versão do Python
- Para ajustar quais testes rodam na pipeline

---

### 📦 `fixtures/` — Dados de Configuração e Massa de Testes

Esta pasta armazena **dados externos** que alimentam os testes. A separação de dados
do código permite reutilizar os mesmos testes em ambientes diferentes sem alterar nenhum `.robot`.

| Arquivo | Descrição | Vai pro Git? |
|---------|-----------|:------------:|
| `data.yaml.example` | Modelo de credenciais com placeholders | ✅ Sim |
| `data.yaml` | Credenciais reais (email e senha) | ❌ Não |
| `env.yaml` | URLs dos ambientes (API e Front) | ✅ Sim |

#### `data.yaml.example`
```yaml
Login:
  USER: seu_email@qacoders.com
  PASSWORD: sua_senha_aqui
```
Serve como **referência** para o aluno saber o formato esperado. Ele deve copiar
este arquivo para `data.yaml` e preencher com dados reais.

#### `data.yaml`
Contém as credenciais reais de acesso. Está no `.gitignore` para **nunca** ser
versionado. Cada pessoa tem o seu localmente.

#### `env.yaml`
Define os ambientes disponíveis. Cada turma tem seu ambiente com URLs próprias:
```yaml
environments:
  SuaTurma:
    Swagger: https://api-sua-turma.qacoders.dev.br/api/    # URL da API
    ERPFront: https://sua-turma.qacoders.dev.br/login      # URL do Front
```

**Como o ambiente é selecionado:**
O script `get_config.py` lê o parâmetro `--env` e retorna o nome do ambiente.
Os resources usam esse valor para buscar a URL correta no `env.yaml`.

---

### 🖥️ `pages/` — Page Objects (Mapeamento de Elementos Web)

| Arquivo | Descrição |
|---------|-----------|
| `pages_web.resource` | Variáveis com locators (XPath/CSS) dos elementos da interface |

**Conceito:** O padrão Page Object separa a **localização dos elementos** da
**lógica de interação**. Se um botão mudar de ID no sistema, você corrige
**apenas aqui** — os testes continuam funcionando sem alteração.

**Exemplo:**
```robot
${emaillogin}       //input[@id='email']
${buttonEntrar}     //button[@id='login']
${cpfInput}         //input[@id='cpf']
```

**Quando editar:**
- Quando um elemento da interface mudar (ID, classe, XPath)
- Quando mapear novos elementos para novos cenários Web

**Boas práticas:**
- Use nomes descritivos nas variáveis (`${buttonSalvar}`, não `${btn1}`)
- Prefira locators por ID (mais estáveis) sobre XPath posicional
- Agrupe elementos por página/seção com comentários

---

### ⚙️ `resources/` — Keywords Reutilizáveis

Esta é a **camada de lógica** do projeto. Cada arquivo `.resource` agrupa keywords
relacionadas a um módulo ou funcionalidade.

---

#### `keywords.resource` — Keywords Globais

**O arquivo mais importante.** Contém:

| Keyword | O que faz |
|---------|-----------|
| `Criar Sessao` | Abre uma sessão HTTP com a URL do ambiente configurado |
| `Pegar Token` | Faz login via API e retorna o token JWT de autenticação |
| `Create User` | Cria um usuário com dados fake e retorna o ID |
| `Create Company` | Cria uma empresa com dados fake e retorna o ID |
| `Create Board` | Cria uma diretoria com dados fake e retorna o ID |

**Importações:**
```robot
Library      RequestsLibrary              # Chamadas HTTP
Library      String                       # Manipulação de strings
Library      Collections                  # Listas e dicionários
Library      OperatingSystem              # Operações de sistema
Library      ../tests/get_config.py       # Seleção de ambiente
Library      ../resources/libs/get_fake_person.py  # Dados fake

Variables    ../fixtures/data.yaml        # Credenciais
Variables    ../fixtures/env.yaml         # URLs dos ambientes
```

---

#### `users.resource` — Keywords do Módulo Usuário

| Keyword | Verbo HTTP | O que faz |
|---------|:----------:|-----------|
| `List Users` | GET | Lista todos os usuários |
| `Count Users` | GET | Retorna a contagem total |
| `Get User` | GET | Busca um usuário por ID |
| `Delete User` | DELETE | Remove um usuário por ID |
| `Put Status` | PUT | Atualiza status (ativo/inativo) |
| `Cadastro Sucesso` | POST+GET+DELETE | Fluxo completo: cria, valida e remove |

---

#### `company.resource` — Keywords do Módulo Empresa

| Keyword | Verbo HTTP | O que faz |
|---------|:----------:|-----------|
| `List Company` | GET | Lista todas as empresas |
| `Count Company` | GET | Retorna a contagem total |
| `Get Company` | GET | Busca uma empresa por ID |
| `Delete Company` | DELETE | Remove uma empresa por ID |
| `Put Status` | PUT | Atualiza status da empresa |
| `Editar Company` | PUT | Atualiza endereço da empresa |
| `Cadastar empresa campo cnpj vazio` | POST | Cenário negativo (campo obrigatório vazio) |
| `Validar Id inesistente` | GET | Cenário negativo (ID inexistente) |

---

#### `board.resource` — Keywords do Módulo Diretoria

| Keyword | Verbo HTTP | O que faz |
|---------|:----------:|-----------|
| `Criar Board` | POST | Cria uma diretoria |
| `List Board` | GET | Lista todas as diretorias |
| `Count Board` | GET | Retorna a contagem |
| `Get Board` | GET | Busca uma diretoria por ID |
| `Editar Board` | PUT | Atualiza o nome da diretoria |

---

#### `web.resource` — Keywords de Interação Web

Contém keywords que simulam ações do usuário no navegador usando Selenium:

| Grupo | Keywords |
|-------|----------|
| Navegação | `Abrir navegador`, `Fechar navegador` |
| Login | Passos 1 a 4 (acessar, digitar email/senha, clicar entrar) |
| Cadastro Usuário | Passos 5 a 14 (navegar menus, preencher formulário, salvar) |
| Cadastro Empresa | Passos 6 a 23 (preencher formulário completo com endereço) |
| Edição | Passo 7.1 (clicar em editar e alterar nome) |
| Pesquisa | Passo 7 (pesquisar no campo de busca) |

**Importações específicas:**
```robot
Library    SeleniumLibrary    # Automação de navegador
Library    XML                # Parsing de XML se necessário
Resource   ../pages/pages_web.resource  # Locators dos elementos
```

---

#### `resources/libs/` — Bibliotecas Python Auxiliares

| Arquivo | O que faz |
|---------|-----------|
| `get_fake_person.py` | Gera dados brasileiros aleatórios usando a lib Faker |

**Funções disponíveis:**

| Função | Retorno |
|--------|---------|
| `get_fake_person()` | Dicionário com `name`, `email`, `cpf` |
| `get_fake_company()` | Dicionário com `nome_empresa`, `cnpj`, `telefone`, `email`, endereço completo |
| `get_fake_board()` | String com nome aleatório de diretoria |

**Por que usar dados fake?**
- Cada execução gera dados únicos, evitando conflitos de duplicidade
- Não depende de dados pré-cadastrados no banco
- Testes ficam independentes entre si

---

### 🧪 `tests/` — Suítes de Teste

Aqui ficam os arquivos `.robot` com os **cenários de teste**. É a camada mais alta
da pirâmide — deve ser legível e descritiva, delegando lógica para os `resources/`.

---

#### `tests/api_tests/` — Testes de API

Testam endpoints REST diretamente (sem interface visual).

| Arquivo | Cenários |
|---------|----------|
| `user.robot` | Criar, buscar por ID, listar, contar, atualizar status |
| `company.robot` | Criar, buscar, listar, contar, editar, validar campo vazio, ID inexistente |
| `board.robot` | Criar, buscar por ID, listar, contar, atualizar nome |

**Exemplo de cenário:**
```robot
Criar usuário com sucesso
    Cadastro Sucesso    # Chama keyword que cria, valida e deleta
```

---

#### `tests/web_tests/` — Testes Web

Testam a interface do sistema via navegador (Selenium).

| Arquivo | Cenários |
|---------|----------|
| `user.robot` | Cadastro, edição e pesquisa de usuário |
| `company.robot` | Cadastro e edição de empresa |

**Características:**
- Usam `Test Setup` para abrir o navegador antes de cada teste
- Usam `Test Teardown` para fechar o navegador após cada teste
- Cada cenário é uma sequência de passos numerados (legibilidade)

---

#### Arquivos auxiliares em `tests/`

| Arquivo | O que faz |
|---------|-----------|
| `get_config.py` | Recebe `--env NomeDaTurma` e retorna o nome do ambiente selecionado |
| `run.py` | Script alternativo que executa os testes passando o ambiente como argumento |

---

## 🔄 Fluxo de Dependência entre Camadas

```
┌─────────────────────────────────────────────────────────┐
│  tests/*.robot (cenários de teste)                      │
│    └── importa resources/*.resource (keywords)          │
│          ├── importa fixtures/*.yaml (dados/config)     │
│          ├── importa resources/libs/*.py (geradores)    │
│          └── importa pages/*.resource (locators Web)    │
└─────────────────────────────────────────────────────────┘
```

**Regra de ouro:** Cada camada tem UMA responsabilidade:

| Camada | Responsabilidade | Quando editar |
|--------|-----------------|---------------|
| `tests/` | Definir **o quê** testar | Novo cenário de teste |
| `resources/` | Definir **como** testar | Lógica de keywords |
| `pages/` | Definir **onde** interagir | Elemento da UI mudou |
| `fixtures/` | Definir **com quais dados** | Trocar ambiente/credenciais |
| `libs/` | **Gerar** dados dinâmicos | Novo tipo de dado fake |

---

## 📁 Arquivos da Raiz

| Arquivo | Papel |
|---------|-------|
| `.gitignore` | Define o que o Git ignora (credenciais, cache, resultados, venv) |
| `README.md` | Documentação principal: setup, execução, fluxo de branches |
| `STRUCTURE.md` | Este arquivo: explicação detalhada da arquitetura |
| `requirements.txt` | Lista de dependências Python com versões |

---

## 🧩 Resumo Visual

```
ALUNO configura:    fixtures/data.yaml + fixtures/env.yaml
                           │
                           ▼
TESTES usam:        tests/api_tests/*.robot  OU  tests/web_tests/*.robot
                           │
                           ▼
KEYWORDS fazem:     resources/*.resource  (lógica de negócio)
                           │
                    ┌──────┼──────┐
                    ▼      ▼      ▼
               libs/    pages/   fixtures/
             (dados)  (locators) (config)
```
