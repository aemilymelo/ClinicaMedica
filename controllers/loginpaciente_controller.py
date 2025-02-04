from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Prontuario  

# Criando o Blueprint para o login dos pacientes
loginpaciente_bp = Blueprint('loginpaciente', __name__, template_folder='../templates')

# Lista de pacientes e senhas (exemplo)
pacientes = {
    "eduarda": "eduarda",
    "emily": "emilyutfpr",
    "lucas": "lucas123"
}

# Rota de Login para pacientes
@loginpaciente_bp.route('/loginpaciente', methods=['GET', 'POST'])
def loginpaciente():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in pacientes and pacientes[username] == password:
            session['paciente'] = username  
            return redirect(url_for('loginpaciente.portal_paciente'))  
        else:
            return "Usuário ou senha incorretos", 401  
    
    return render_template('loginpaciente.html')

# Rota para o portal do paciente (após login bem-sucedido)
@loginpaciente_bp.route('/portal_paciente')
def portal_paciente():
    if 'paciente' not in session:
        return redirect(url_for('loginpaciente.loginpaciente'))  

    usuario_logado = session['paciente']

    paciente = {
        'nome': usuario_logado.capitalize(),
        'idade': 25,
        'prontuario': Prontuario.query.all()  
    }

    return render_template('portal_paciente.html', paciente=paciente)

@loginpaciente_bp.route('/logout_paciente')
def logout_paciente():
    session.pop('paciente', None)  
    return redirect(url_for('index.html'))  
