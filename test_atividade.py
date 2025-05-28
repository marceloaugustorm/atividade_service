import unittest
from app import app, db
from models.atividade_model import Atividade, Resposta

class AtividadeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["TESTING"] = True

        with self.app.app_context():
            db.create_all()

            
            atividade = Atividade(id_disciplina=1, enunciado="Teste de atividade")
            resposta1 = Resposta(id_aluno=1, resposta="arquivo1.zip", nota=8.5, atividade=atividade)
            resposta2 = Resposta(id_aluno=2, resposta="arquivo2.zip", atividade=atividade)

            db.session.add(atividade)
            db.session.add(resposta1)
            db.session.add(resposta2)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_listar_atividades(self):
        response = self.client.get("/atividades")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['enunciado'], "Teste de atividade")
        self.assertEqual(len(data[0]['respostas']), 2)

    def test_obter_atividade_existente(self):
        response = self.client.get("/atividades/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id_atividade'], 1)
        self.assertEqual(data['enunciado'], "Teste de atividade")

        # Verifica que existe o campo respostas e é uma lista
        self.assertIn('respostas', data)
        self.assertIsInstance(data['respostas'], list)
        self.assertEqual(len(data['respostas']), 2)

        # Verifica alguns campos da primeira resposta
        primeira_resposta = data['respostas'][0]
        self.assertIn('id_aluno', primeira_resposta)
        self.assertIn('resposta', primeira_resposta)
        self.assertIn('nota', primeira_resposta)

    def test_obter_atividade_inexistente(self):
        response = self.client.get("/atividades/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("erro", response.get_json())

if __name__ == "__main__":
    unittest.main()
