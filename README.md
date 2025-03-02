# Flix API

Flix API é uma API RESTful desenvolvida com Django REST Framework para gerenciar um catálogo de filmes. A API permite cadastrar, buscar, filtrar e avaliar filmes, além de contar com autenticação de usuários e documentação interativa.

## Funcionalidades

- **CRUD completo** para filmes, gêneros, atores e avaliações.
- **Busca avançada** por título, gênero, popularidade e data de lançamento.
- **Autenticação JWT** para garantir segurança no acesso.
- **Controle de permissões** para diferentes níveis de usuários.
- **Avaliação de filmes** para que os usuários possam dar notas e opiniões.
- **Documentação interativa** com Swagger.

## Tecnologias Utilizadas

- **Django** + **Django REST Framework**
- **PostgreSQL** como banco de dados
- **Docker** para gerenciamento de containers
- **JWT (JSON Web Token)** para autenticação
- **Swagger** para documentação interativa

## Instalação e Configuração

### 1️⃣ Clonar o repositório:
```bash
git clone https://github.com/seu-usuario/flix-api.git
cd flix-api
```

### 2️⃣ Criar e ativar um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as dependências:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados:
```bash
python manage.py migrate
```

### 5️⃣ Criar um superusuário para acessar a administração:
```bash
python manage.py createsuperuser
```

### 6️⃣ Iniciar o servidor de desenvolvimento:
```bash
python manage.py runserver
```
A API estará disponível em: `http://127.0.0.1:8000/`

## Uso com Docker

Se preferir rodar o projeto em um ambiente isolado, utilize **Docker**:

```bash
docker-compose up --build
```
A API estará rodando no contêiner e acessível na porta configurada.

## Documentação

A documentação interativa pode ser acessada em:
- **Swagger UI**: `http://127.0.0.1:8000/swagger/`
