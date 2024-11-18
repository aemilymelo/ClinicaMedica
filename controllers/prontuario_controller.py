from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Prontuario, Paciente
from datetime import datetime

# Criação do Blueprint para o prontuário
prontuario_bp = Blueprint('prontuario', __name__, url_prefix='/prontuarios')

# Rota para listar prontuários
@prontuario_bp.route('/')
def listar_prontuarios():
    prontuarios = Prontuario.query.all()  # Recuperando todos os prontuários do banco
    return render_template('listar_prontuarios.html', prontuarios=prontuarios)

# Rota para adicionar prontuário
@prontuario_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar_prontuario():
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data_str = request.form['data']
        diagnostico = request.form['diagnostico']
        prescricoes = request.form['prescricoes']

        # Convertendo a data de string para o tipo datetime.date
        data = datetime.strptime(data_str, '%Y-%m-%d').date()

        # Criando o novo prontuário
        prontuario = Prontuario(
            paciente_id=paciente_id,
            data=data,
            diagnostico=diagnostico,
            prescricoes=prescricoes
        )
        
        # Adicionando ao banco de dados
        db.session.add(prontuario)
        db.session.commit()

        flash('Prontuário adicionado com sucesso!', 'success')  # Mensagem de sucesso
        return redirect(url_for('prontuario.listar_prontuarios'))

    # Passando os pacientes para o formulário
    pacientes = Paciente.query.all()
    return render_template('adicionar_prontuario.html', pacientes=pacientes)

# Rota para editar prontuário
@prontuario_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_prontuario(id):
    prontuario = Prontuario.query.get_or_404(id)  # Buscando o prontuário a ser editado
    pacientes = Paciente.query.all()  # Recuperando a lista de pacientes

    if request.method == 'POST':
        prontuario.paciente_id = request.form['paciente_id']
        
        # Convertendo a data de string para o tipo datetime.date
        data_str = request.form['data']
        prontuario.data = datetime.strptime(data_str, '%Y-%m-%d').date()
        
        prontuario.diagnostico = request.form['diagnostico']
        prontuario.prescricoes = request.form['prescricoes']

        # Atualizando o banco de dados
        db.session.commit()

        flash('Prontuário atualizado com sucesso!', 'success')  # Mensagem de sucesso
        return redirect(url_for('prontuario.listar_prontuarios'))

    return render_template('editar_prontuario.html', prontuario=prontuario, pacientes=pacientes)

# Rota para deletar prontuário
@prontuario_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar_prontuario(id):
    prontuario = Prontuario.query.get_or_404(id)  # Buscando o prontuário a ser deletado

    # Removendo o prontuário do banco de dados
    db.session.delete(prontuario)
    db.session.commit()

    flash('Prontuário deletado com sucesso!', 'success')  # Mensagem de sucesso
    return redirect(url_for('prontuario.listar_prontuarios'))
