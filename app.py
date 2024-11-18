from flask import Flask, render_template
from models import db # Certifique-se de importar a instância do SQLAlchemy
from controllers.paciente_controller import paciente_bp
from controllers.login_controller import login_bp  # Importando o Blueprint do login
from controllers.agendamento_controller import agendamento_bp
from controllers.consulta_controller import consulta_bp
from controllers.prontuario_controller import prontuario_bp


app = Flask(__name__)

app.secret_key = 'b5eea9be20af8495f4cc049a501050c2621c0b7c8eb3ef16'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando a instância do banco de dados com o app Flask
db.init_app(app)

# Registrando o Blueprint
app.register_blueprint(paciente_bp)
app.register_blueprint(login_bp)
app.register_blueprint(agendamento_bp)
app.register_blueprint(consulta_bp)
app.register_blueprint(prontuario_bp)





@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas se ainda não existirem
    app.run(debug=True)
