# Camp ProgComp UFMG

Plataforma para montar problemsets do Codeforces com problemas que os competidores ainda não resolveram.

## Estrutura do projeto

```
camp-progcomp-ufmg/
├── backend/          # API Django
├── frontend/         # React (em desenvolvimento)
└── README.md
```

## Pré-requisitos

- **Python 3.11+** (recomendado 3.12 ou 3.13)
- **Git**
- **Node.js 20+** (quando for trabalhar no frontend)

## Instalação do Python

### macOS (Homebrew)

```bash
brew install python
python3 --version
```

### macOS / Windows / Linux

Baixe o instalador em [python.org/downloads](https://www.python.org/downloads/) e confirme no terminal:

```bash
python3 --version
pip3 --version
```

## Configuração do backend

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd camp-progcomp-ufmg
```

### 2. Criar e ativar o ambiente virtual

O ambiente virtual isola as dependências do projeto na pasta `backend/.venv`.

```bash
cd backend
python3 -m venv .venv
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Com o ambiente ativo, o terminal exibe `(.venv)` no início da linha.

Para sair do ambiente virtual:

```bash
deactivate
```

### 3. Instalar dependências

Com o `.venv` ativo, instale os pacotes listados em `requirements.txt` (inclui Django, Django REST Framework, JWT, Postgres, etc.):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verificar instalação do Django

```bash
python -m django --version
```

### 5. Aplicar migrations do banco

```bash
python manage.py migrate
```

### 6. Subir o servidor de desenvolvimento

```bash
python manage.py runserver
```

A API ficará disponível em [http://localhost:8000](http://localhost:8000).

### 7. (Opcional) Criar superusuário para o Django Admin

```bash
python manage.py createsuperuser
```

Acesse [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Dependências principais (`requirements.txt`)

| Pacote | Uso |
|--------|-----|
| Django | Framework web / API |
| djangorestframework | API REST |
| djangorestframework_simplejwt | Autenticação JWT |
| psycopg2-binary | Driver PostgreSQL |
| django-cors-headers | CORS para o frontend |
| python-dotenv | Variáveis de ambiente |
| requests | Integração com API do Codeforces |

## IDE (Cursor / VS Code)

Selecione o interpretador Python do projeto:

1. `Cmd + Shift + P` → **Python: Select Interpreter**
2. Escolha `backend/.venv/bin/python`

Isso habilita autocomplete e resolve imports do Django.

## Comandos úteis

```bash
# Ativar venv (a partir de backend/)
source .venv/bin/activate

# Instalar nova dependência e atualizar requirements.txt
pip install <pacote>
pip freeze > requirements.txt

# Criar migrations após alterar models
python manage.py makemigrations
python manage.py migrate

# Shell interativo do Django
python manage.py shell
```

## Frontend

O frontend React será adicionado na pasta `frontend/`. Instruções de setup serão incluídas quando o scaffold estiver pronto.
