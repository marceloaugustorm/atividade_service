from database import db
from flask import request, jsonify

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aluno = db.Column(db.Integer, nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    nota = db.Column(db.Float, nullable=True)
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'), nullable=False)

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_disciplina = db.Column(db.Integer, nullable=False)
    enunciado = db.Column(db.String(255), nullable=False)
    respostas = db.relationship('Resposta', backref='atividade', cascade="all, delete-orphan")

    @staticmethod
    def listar():
        return Atividade.query.all()

    @staticmethod
    def obter(id_atividade):
        return Atividade.query.filter_by(id=id_atividade).first()
    
    @staticmethod
    def criar_com_respostas(id_disciplina, enunciado, respostas):
        nova_atividade = Atividade(id_disciplina=id_disciplina, enunciado=enunciado)
        for r in respostas:
            resposta = Resposta(
                id_aluno=r.get("id_aluno"),
                resposta=r.get("resposta"),
                nota=r.get("nota")
            )
            nova_atividade.respostas.append(resposta)

        db.session.add(nova_atividade)
        db.session.commit()
        return nova_atividade