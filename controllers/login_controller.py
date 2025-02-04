from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Prontuario

# Criando o Blueprint para o login
login_bp = Blueprint('login', __name__, template_folder='../templates')

# Lista de médicos e senhas
medicos = {
    "emily": "emilyutfpr",
    "eduarda" : "eduarda",
    "maria": "mariautfpr"
}

# Rota de Login
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o nome de usuário e senha estão corretos
        if username in medicos and medicos[username] == password:
            session['medico'] = username  # 🔹 Armazena o médico na sessão
            return redirect(url_for('login.dashboard'))
        else:
            return "Usuário ou senha incorretos", 401  
    
    return render_template('login.html')

# Rota para o painel do médico
@login_bp.route('/dashboard')
def dashboard():
    if 'medico' not in session:  # 🔹 Verifica se há um médico autenticado
        return redirect(url_for('login.login'))
    
    medico = {
        'foto': 'url_da_imagem_do_medico.jpg',
        'nome': session['medico'],  # 🔹 Usa o nome do médico autenticado
        'crm': 'CRM 123456',
        'especialidade': 'Cardiologia'
    }
    return render_template('dashboard.html', medico=medico, Prontuario=Prontuario)

# Rota para Logout
@login_bp.route('/logout_medico')
def logout_medico():
    session.pop('medico', None)  # 🔹 Remove o médico da sessão
    return redirect(url_for('index.html'))
