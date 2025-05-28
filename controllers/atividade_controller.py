from flask import Blueprint, jsonify
from models.atividade_model import Atividade
from clients.pessoa_service_client import PessoaServiceClient
from flask import request

atividade_bp = Blueprint("atividade_bp", __name__)

@atividade_bp.route("/atividades", methods=["GET"])
def listar_atividades():
    atividades = Atividade.listar()
    return jsonify([
        {
            "id_atividade": a.id,
            "id_disciplina": a.id_disciplina,
            "enunciado": a.enunciado,
            "respostas": [
                {"id_aluno": r.id_aluno, "resposta": r.resposta, "nota": r.nota}
                for r in a.respostas
            ]
        } for a in atividades
    ])

@atividade_bp.route("/atividades/<int:id_atividade>", methods=["GET"])
def obter_atividade(id_atividade):
    a = Atividade.obter(id_atividade)
    if not a:
        return jsonify({"erro": "Atividade não encontrada"}), 404
    return jsonify({
        "id_atividade": a.id,
        "id_disciplina": a.id_disciplina,
        "enunciado": a.enunciado,
        "respostas": [
            {"id_aluno": r.id_aluno, "resposta": r.resposta, "nota": r.nota}
            for r in a.respostas
        ]
    })


@atividade_bp.route("/testar-conexao/<int:id_professor>/<int:id_disciplina>", methods=["GET"])
def testar_conexao(id_professor, id_disciplina):
    leciona = PessoaServiceClient.verificar_leciona(id_professor, id_disciplina)
    return jsonify({"leciona": leciona})


@atividade_bp.route("/atividades", methods=["POST"])
def criar_atividade():
    dados = request.get_json()
    id_disciplina = dados.get("id_disciplina")
    enunciado = dados.get("enunciado")
    respostas = dados.get("respostas", [])

    if not id_disciplina or not enunciado:
        return jsonify({"erro": "id_disciplina e enunciado são obrigatórios"}), 400

    nova_atividade = Atividade.criar_com_respostas(id_disciplina, enunciado, respostas)

    return jsonify({
        "msg": "Atividade criada com sucesso",
        "id_atividade": nova_atividade.id
    }), 201




