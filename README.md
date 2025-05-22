# 📘 API de Atividades

API desenvolvida em Flask para gerenciamento e exibição de atividades acadêmicas. Esta API é parte de um ecossistema de microsserviços e possui integração com a API de Pessoas para validação de professores.

---

## 📄 Descrição da API

A API de Atividades permite:

- 🔍 Listar todas as atividades  
- 📑 Buscar uma atividade específica  
- 🧑‍🏫 Visualizar uma atividade conforme permissões do professor (verificação com API externa)

---

## 🚀 Instruções de Execução (com Docker)

### Pré-requisitos

- [Docker](https://www.docker.com/) instalado

### Passos:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-atividade.git
cd api-atividade
```

2. Crie um arquivo `requirements.txt` com as dependências:

```txt
flask
requests
```

3. Crie um `Dockerfile` na raiz do projeto:

```Dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
```

4. Crie um `app.py` com o seguinte conteúdo:

```python
from flask import Flask
from atividade_routes import atividade_bp

app = Flask(__name__)
app.register_blueprint(atividade_bp, url_prefix="/atividades")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

5. Estrutura de diretórios recomendada:

```
api-atividade/
├── app.py
├── atividade_routes.py
├── models/
│   └── atividade_model.py
├── clients/
│   └── pessoa_service_client.py
├── requirements.txt
└── Dockerfile
```

---

## 🔗 Integração com Microsserviços

Esta API se comunica com o **serviço de Pessoas** através do `PessoaServiceClient` para verificar se o professor leciona determinada disciplina. Se não leciona, o campo `respostas` é omitido da resposta.

Exemplo de chamada protegida:
```
GET /atividades/5/professor/3
```

---

## 🧪 Endpoints

| Método | Rota                                                   | Descrição                                                                 |
|--------|--------------------------------------------------------|---------------------------------------------------------------------------|
| GET    | `/atividades/`                                         | Lista todas as atividades                                                |
| GET    | `/atividades/<id_atividade>`                           | Retorna uma atividade específica                                         |
| GET    | `/atividades/<id_atividade>/professor/<id_professor>` | Retorna a atividade com/sem respostas conforme permissões do professor  |

---

## 📌 Observações

- A API responde com status `404` caso a atividade não seja encontrada.
- A validação do professor é feita consultando a API de Pessoas.

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
