```
# 📘 API de Atividades

API Flask para gerenciamento de atividades acadêmicas. Este serviço faz parte de um ecossistema de microsserviços e integra-se com o serviço de Pessoas para validar o acesso de professores.

---

## 📄 Funcionalidades

- 🔍 Listagem de atividades
- 📑 Consulta de atividade por ID
- 🧑‍🏫 Exibição de atividade com validação de permissão via API externa
- 📝 Criação de novas atividades com respostas associadas

---

## 🏗️ Arquitetura

A aplicação utiliza a **fábrica de aplicação** (`create_app`) para configurar e iniciar a API. As rotas são organizadas por meio de **blueprints**, com a seguinte estrutura:

```python
from config import create_app
from controllers.atividade_controller import atividade_bp

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    app.run(host='localhost', port=5002)
```

---

## 🚀 Executando com Docker

### 📦 Pré-requisitos

- Docker instalado

### 📁 Estrutura esperada

```
api-atividade/
├── app.py
├── config.py
├── controllers/
│   └── atividade_controller.py
├── models/
│   └── atividade_model.py
├── clients/
│   └── pessoa_service_client.py
├── requirements.txt
└── Dockerfile
```

### 🧪 `requirements.txt`

```
flask
requests
```

### 🐳 `Dockerfile`

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python", "app.py"]
```

### ▶️ Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/atividade_service.git
cd atividade_service
```

2. Construa a imagem Docker:

```bash
docker build -t atividade_service . 
```

3. Rode o container:

```bash
docker run -d -p 5002:5002 atividade_service
```

A API estará acessível em: `http://localhost:5002/atividades`

---

## 🔗 Integração com Microsserviços

Esta API se comunica com o **serviço de Pessoas** através do `PessoaServiceClient`, para verificar se um professor tem permissão para visualizar determinadas atividades.  
Se não leciona a disciplina, o campo `respostas` será ocultado da resposta.

---

## 🧪 Endpoints

| Método | Rota                                                   | Descrição                                                                 |
|--------|--------------------------------------------------------|---------------------------------------------------------------------------|
| GET    | `/atividades/`                                         | Lista todas as atividades                                                |
| GET    | `/atividades/<id_atividade>`                           | Retorna uma atividade específica                                         |
| GET    | `/atividades/<id_atividade>/professor/<id_professor>` | Retorna a atividade filtrando dados com base no professor                |
| POST   | `/atividades/`                                         | Cria uma nova atividade com respostas associadas                         |

---

## 📌 Observações

- A lógica de inicialização da aplicação está separada em `config.py`, seguindo o padrão **Flask Factory**.
- As rotas estão organizadas no módulo `controllers/atividade_controller.py`.

---

## 📜 Licença

Este projeto está sob a licença MIT.
```
