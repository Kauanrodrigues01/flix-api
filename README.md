# 🎬 Flix API

Uma API REST completa para gerenciamento de filmes, atores, gêneros e avaliações, desenvolvida com Django REST Framework.

[![Django](https://img.shields.io/badge/Django-5.1.5-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13.1-blue.svg)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.15.2-red.svg)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

## 📋 Sobre o Projeto

A Flix API é uma aplicação web que oferece um sistema completo para catalogação e avaliação de filmes. A API permite o gerenciamento de:

- **Filmes** com informações detalhadas (título, gênero, data de lançamento, resumo)
- **Atores** com dados pessoais e nacionalidade
- **Gêneros** para categorização dos filmes
- **Avaliações** dos usuários com sistema de estrelas (0-5) e comentários
- **Autenticação** com JWT para controle de acesso

## ✨ Principais Funcionalidades

### 🎭 Gestão de Atores
- CRUD completo para atores
- Suporte a 50+ nacionalidades
- Filtros por nome e filme
- Importação em lote via CSV
- Validações de data de nascimento

### 🎬 Gestão de Filmes
- CRUD completo para filmes
- Associação com múltiplos atores e gêneros
- Sistema de avaliação integrado
- Filtros avançados (título, gênero, ano, atores)
- Estatísticas de filmes e avaliações

### 🎯 Sistema de Gêneros
- Gestão de categorias de filmes
- Proteção contra exclusão com filmes vinculados
- Filtros de busca

### ⭐ Sistema de Avaliações
- Avaliações de 0 a 5 estrelas
- Comentários opcionais
- Filtros por filme e nota
- Permissões para edição apenas pelo autor

### 🔐 Autenticação e Autorização
- Autenticação JWT com refresh tokens
- Sistema de permissões granular
- Registro de usuários
- Blacklist de tokens

## 🚀 Tecnologias Utilizadas

### Backend
- **Django 5.1.5** - Framework web principal
- **Django REST Framework 3.15.2** - API REST
- **django-filter 24.3** - Filtros avançados
- **Simple JWT 5.4.0** - Autenticação JWT
- **drf-yasg 1.21.8** - Documentação Swagger

### Banco de Dados
- **PostgreSQL** (produção)
- **SQLite** (desenvolvimento)
- **psycopg2-binary 2.9.10** - Driver PostgreSQL

### Servidor
- **uWSGI 2.0.28** - Servidor WSGI
- **Docker** - Containerização
- **Docker Compose** - Orquestração

### Utilitários
- **python-decouple 3.8** - Configurações via ambiente
- **dj-database-url 2.3.0** - URLs de banco de dados
- **pandas 2.2.3** - Manipulação de dados CSV

## 📊 Estrutura da API

### Endpoints Principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET/POST` | `/api/v1/actors/` | Listar/Criar atores |
| `GET/PUT/DELETE` | `/api/v1/actors/{id}/` | Detalhar/Atualizar/Excluir ator |
| `GET/POST` | `/api/v1/movies/` | Listar/Criar filmes |
| `GET/PUT/DELETE` | `/api/v1/movies/{id}/` | Detalhar/Atualizar/Excluir filme |
| `GET` | `/api/v1/movies/stats/` | Estatísticas de filmes |
| `GET/POST` | `/api/v1/genres/` | Listar/Criar gêneros |
| `GET/PUT/DELETE` | `/api/v1/genres/{id}/` | Detalhar/Atualizar/Excluir gênero |
| `GET/POST` | `/api/v1/reviews/` | Listar/Criar avaliações |
| `GET/PUT/DELETE` | `/api/v1/reviews/{id}/` | Detalhar/Atualizar/Excluir avaliação |

### Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/api/token/` | Obter token de acesso |
| `POST` | `/api/token/refresh/` | Renovar token |
| `POST` | `/api/token/verify/` | Verificar token |
| `POST` | `/api/token/blacklist/` | Invalidar token |
| `POST` | `/api/users/` | Registrar usuário |

## 🔧 Instalação e Configuração

### Pré-requisitos

- Python 3.13+
- Docker e Docker Compose (opcional)
- PostgreSQL (para produção)

### 🐳 Execução com Docker (Recomendado)

1. **Clone o repositório:**
```bash
git clone https://github.com/Kauanrodrigues01/flix-api.git
cd flix-api
```

2. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
```

3. **Execute com Docker Compose:**
```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8000`

### 🐍 Execução Local

1. **Clone e configure o ambiente:**
```bash
git clone https://github.com/Kauanrodrigues01/flix-api.git
cd flix-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure o banco de dados:**
```bash
python manage.py migrate
```

4. **Crie um superusuário:**
```bash
python manage.py createsuperuser
```

5. **Execute o servidor:**
```bash
python manage.py runserver
```

### 📥 Importação de Dados

Para importar atores a partir do arquivo CSV:

```bash
python manage.py import_actors actors.csv
```

## 📖 Documentação da API

A documentação interativa da API está disponível em:

- **Swagger UI**: `http://localhost:8000/swagger/`
- **Admin Django**: `http://localhost:8000/admin/`

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
# Django Settings
SECRET_KEY='sua-chave-secreta-aqui'
DEBUG=True
ALLOWED_HOSTS=*
LANGUAGE_CODE='pt-br'
TIME_ZONE='America/Fortaleza'

# Database
DATABASE_URL=postgresql://usuario:senha@localhost:5432/flixdb

# JWT Settings
ACCESS_TOKEN_LIFETIME_SECONDS=3600
REFRESH_TOKEN_LIFETIME_SECONDS=7200
```

## 📝 Exemplos de Uso

### Registrar um usuário

```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@email.com",
    "full_name": "Nome do Usuário",
    "password": "senhaSegura123"
  }'
```

### Obter token de acesso

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@email.com",
    "password": "senhaSegura123"
  }'
```

### Criar um filme

```bash
curl -X POST http://localhost:8000/api/v1/movies/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer SEU_TOKEN_AQUI" \
  -d '{
    "title": "Vingadores: Ultimato",
    "genre": "uuid-do-genero",
    "release_date": "2019-04-26",
    "resume": "Os heróis mais poderosos da Terra...",
    "actors": ["uuid-ator-1", "uuid-ator-2"]
  }'
```

### Filtrar filmes

```bash
# Por gênero
curl "http://localhost:8000/api/v1/movies/?genre=uuid-do-genero"

# Por ano
curl "http://localhost:8000/api/v1/movies/?release_year=2019"

# Por ator
curl "http://localhost:8000/api/v1/movies/?actors=uuid-do-ator"
```

## 🧪 Desenvolvimento

### Executar testes

```bash
python manage.py test
```

### Verificar código com flake8

```bash
flake8
```

### Estrutura do Projeto

```
flix-api/
├── accounts/          # Autenticação e usuários
├── actors/           # Gestão de atores
├── genres/           # Gestão de gêneros
├── movies/           # Gestão de filmes
├── reviews/          # Sistema de avaliações
├── utils/            # Utilitários (paginação)
├── app/              # Configurações principais
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Kauan Rodrigues Lima**

- GitHub: [@Kauanrodrigues01](https://github.com/Kauanrodrigues01)
- LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/kauan-rodrigues-lima/)
