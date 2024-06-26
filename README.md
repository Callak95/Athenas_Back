
# Sistema de Gerenciamento de Pessoas - Backend (Athenas Test)

Este projeto é o backend de um sistema de gerenciamento de pessoas desenvolvido utilizando Django e Django REST framework. Ele fornece uma API para realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados de pessoas.

## Tecnologias Utilizadas

- Python 3.12
- Django 5.0
- Django REST framework
- PostgreSQL

## Requisitos

- Python 3.12 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/athenas_backend.git
   cd athenas_backend
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   No Windows:
   ```bash
   venv\Scripts\activate
   ```

   No Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. **Migrações:**

   Execute as migrações para criar as tabelas no banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Criação do Superusuário:**

   Crie um superusuário para acessar o admin do Django:

   ```bash
   python manage.py createsuperuser
   ```

## Execução

1. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   O servidor estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Endpoints da API

A API possui os seguintes endpoints para gerenciamento de pessoas:

- `GET /api/pessoas/` - Lista todas as pessoas.
- `POST /api/pessoas/` - Adiciona uma nova pessoa.
- `GET /api/pessoas/<id>/` - Retorna os detalhes de uma pessoa específica.
- `PUT /api/pessoas/<id>/` - Atualiza os dados de uma pessoa específica.
- `DELETE /api/pessoas/<id>/` - Deleta uma pessoa específica.

## Estrutura do Projeto

- `athenas_backend/` - Diretório principal do projeto Django.
- `pessoa/` - Aplicação Django que contém o modelo, views, serializers e URLs relacionados a pessoas.
- `manage.py` - Script de gerenciamento do Django.

## Arquivos Importantes

- `models.py` - Define o modelo Pessoa.
- `serializers.py` - Define o serializer PessoaSerializer.
- `views.py` - Contém as views da API.
- `urls.py` - Define as rotas da API.

## Modelo de Dados

O modelo Pessoa possui os seguintes campos:

- `nome` (CharField) - Nome da pessoa.
- `data_nascimento` (DateField) - Data de nascimento da pessoa.
- `peso` (FloatField) - Peso da pessoa.
- `altura` (FloatField) - Altura da pessoa.
- `sexo` (CharField) - Sexo da pessoa.

## Exemplo de Requisição

### Adicionar uma Pessoa

```bash
POST /api/pessoas/
Content-Type: application/json

{
    "nome": "João Silva",
    "data_nascimento": "1990-01-01",
    "peso": 75.5,
    "altura": 180,
    "sexo": "Masculino"
}
```

### Atualizar uma Pessoa

```bash
PUT /api/pessoas/1/
Content-Type: application/json

{
    "nome": "João Silva",
    "data_nascimento": "1990-01-01",
    "peso": 80,
    "altura": 180,
    "sexo": "Masculino"
}
```

### Deletar uma Pessoa

```bash
DELETE /api/pessoas/1/
```
