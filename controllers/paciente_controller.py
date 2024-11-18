from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Paciente
from datetime import datetime

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

# Rota para listar pacientes
@paciente_bp.route('/')
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('listar_pacientes.html', pacientes=pacientes)

# Rota para adicionar um novo paciente
@paciente_bp.route('/novo', methods=['GET', 'POST'])
def adicionar_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data_nascimento = request.form['data_nascimento']
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        
        novo_paciente = Paciente(
            nome=nome,
            cpf=cpf,
            data_nascimento=datetime.strptime(data_nascimento, '%Y-%m-%d'),
            telefone=telefone,
            endereco=endereco
        )
        
        try:
            db.session.add(novo_paciente)
            db.session.commit()
            flash('Paciente adicionado com sucesso!', 'success')
            return redirect(url_for('paciente.listar_pacientes'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar paciente: {str(e)}', 'error')
            return redirect(url_for('paciente.adicionar_paciente'))

    return render_template('adicionar_paciente.html')

# Rota para editar um paciente
@paciente_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def atualizar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    
    if request.method == 'POST':
        paciente.nome = request.form['nome']
        paciente.cpf = request.form['cpf']
        paciente.data_nascimento = datetime.strptime(request.form['data_nascimento'], '%Y-%m-%d')
        paciente.telefone = request.form.get('telefone')
        paciente.endereco = request.form.get('endereco')

        try:
            db.session.commit()
            flash('Paciente atualizado com sucesso!', 'success')
            return redirect(url_for('paciente.listar_pacientes'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar paciente: {str(e)}', 'error')
            return redirect(url_for('paciente.atualizar_paciente', id=paciente.id))
    
    return render_template('editar_paciente.html', paciente=paciente)

# Rota para deletar um paciente
@paciente_bp.route('/<int:id>/deletar', methods=['POST'])
def deletar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    try:
        db.session.delete(paciente)
        db.session.commit()
        flash('Paciente deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar paciente: {str(e)}', 'error')
    
    return redirect(url_for('paciente.listar_pacientes'))
