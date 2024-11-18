from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(255))
    data_nascimento = db.Column(db.Date, nullable=False)

    prontuarios = db.relationship('Prontuario', backref='paciente', lazy=True)

class Prontuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.String(255))
    prescricoes = db.Column(db.String(255))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
       
    
class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente')  # Status: Pendente, Confirmada, Cancelada
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)

    paciente = db.relationship('Paciente', backref='consultas')

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente')

    paciente = db.relationship('Paciente', backref='agendamentos', lazy=True)
