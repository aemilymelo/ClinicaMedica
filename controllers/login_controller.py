from flask import Blueprint, render_template, request, redirect, url_for

# Criando o Blueprint para o login
login_bp = Blueprint('login', __name__, template_folder='../templates')

# Exemplo de lista de médicos e senhas
medicos = {
    "emily": "emilyutfpr",
    "carlos": "carlosutfpr"
}

# Rota de Login
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o nome de usuário e senha estão corretos
        if username in medicos and medicos[username] == password:
            return redirect(url_for('login.dashboard'))  # Corrigido para 'login.dashboard'
        else:
            return "Usuário ou senha incorretos", 401  
    
    return render_template('login.html')


# Rota para o painel de controle (após login bem-sucedido)
@login_bp.route('/dashboard')
def dashboard():
    # Exemplo de dados para o médico
    medico = {
        'foto': 'url_da_imagem_do_medico.jpg',
        'nome': 'Dr. João Silva',
        'crm': 'CRM 123456',
        'especialidade': 'Cardiologia'
    }
    return render_template('dashboard.html', medico=medico)
