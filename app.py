from flask import Flask
from database import db
from controllers.atividade_controller import atividade_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///atividades.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(atividade_bp)

if __name__ == "__main__":
    app.run(port=5002)
