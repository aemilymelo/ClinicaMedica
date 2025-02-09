from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint


db = SQLAlchemy()

# Modelo para a tabela Paciente
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(255))
    data_nascimento = db.Column(db.Date, nullable=False)

    # Relacionamentos
    prontuarios = db.relationship('Prontuario', backref='paciente_relacao', lazy=True)
    consultas = db.relationship('Consulta', backref='paciente_relacao', lazy=True)
    agendamentos = db.relationship('Agendamento', backref='paciente_relacao', lazy=True)

# Modelo para a tabela Prontuario
class Prontuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.String(255))
    prescricoes = db.Column(db.String(255))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)

    # Relacionamento correto
    paciente = db.relationship('Paciente', backref='prontuarios_relacao')


# Modelo para a tabela Consulta
class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente')  # Status: Pendente, Confirmada, Cancelada
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)

    paciente = db.relationship('Paciente', backref='consultas_relacao')

# Modelo para a tabela Agendamento
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pendente')

    paciente = db.relationship('Paciente', backref='agendamentos_relacao', lazy=True)

# Modelo para a tabela Medico 
class Medico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    especialidade = db.Column(db.String(100))
    

# Modelo para a tabela Relatorio
class Relatorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    telefone = db.Column(db.String(15))
    endereco = db.Column(db.String(255))
    historico = db.Column(db.Text)  # Campo para histórico médico
    queixa = db.Column(db.Text)  # Campo para queixa principal
    exames = db.Column(db.Text)  # Campo para exames realizados
    diagnostico = db.Column(db.Text)  # Campo para diagnóstico
    tratamento = db.Column(db.Text)  # Campo para tratamento
    recomendacoes = db.Column(db.Text)  # Campo para recomendações

    