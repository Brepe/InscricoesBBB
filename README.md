# InscricoesBBB
API em Python, implementando um CRUD simples para receber inscrições do BBB 24.


## Instalação

Necessário possui o Python e pip instalados: 
[Python](https://www.python.org/downloads/), [Pip](https://pip.pypa.io/en/stable/cli/pip_install/)
Caso não possua o MongoDB instalado, veja aqui como instalar:  
[MongoDB](https://www.mongodb.com/docs/manual/installation/)

Depois de ter tudo instalado, siga os passos para rodar o projeto.

- Ative o env com:
```bash
$ source env/Scripts/activate
```
- Instale as bibliotecas
```bash
$ pip install -r requirements.txt
```

- Rode:
```bash
$ python app/main.py
```

## Documentação da API

#### Retorna todos os cadastros

```http
  GET /
```

#### Retorna um cadastro

```http
  GET /user/{email}
```

#### Grava um cadastro

Payload -> { "name": "xxxxx", "password": "xxxxxx","email": "xxxxx","birthday": "xxxxx","region": "xxxxx","termconditions": true,"document": "","photo": "path/to/file/photo1","video": "path/to/file/video1"}

```http
  POST /
```

#### Edita um cadastro

Payload -> { "name": "xxxxx", "birthday": "xxxxx","region": "xxxxx","termconditions": true,"document": "","photo": "path/to/file/photo1","video": "path/to/file/video1"}

```http
  PATCH /user/{email}
```

#### Deleta um cadastro

```http
  DELETE /user/{email}
```