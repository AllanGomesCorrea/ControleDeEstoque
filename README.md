# Controle de Estoque

Ainda em construção.

Objetivo: funcionar como um controle de estoque para um pequeno mercado como exemplo.
Pode ser escalada no futuro.

# Sobre o projeto [PT-BR]

Nesse projeto foi utilizado Django REST framework 

# Tecnologias utilizadas
## Back end
- Python
- Django REST framework
- Banco de dados: SQLite

# Como executar o projeto

## Back end
Pré-requisitos: Django e Python

```bash
# clonar repositório
git clone https://github.com/AllanGomesCorrea/ControleDeEstoque.git

# criar o virtual environment
python3 -m venv venv

# ativar a venv (Linux,macOS)
source venv/bin/activate

# ativar a venv (Windows)
venv\Scripts\activate

# executar o comando para instalação das versões
pip install -r ./requirements.txt

# executar o projeto
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Resultado

Uma collection do Postman foi adicionada aos arquivos para realização dos testes propostos.

# Autor

[![Autor](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/allancorrea/)

Allan Gomes Corrêa

