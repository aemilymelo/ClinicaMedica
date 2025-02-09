from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Agendamento, Paciente
from datetime import datetime

agendamento_bp = Blueprint('agendamento', __name__, url_prefix='/agendamentos')

# Rota para listar agendamentos
@agendamento_bp.route('/')
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return render_template('listar_agendamentos.html', agendamentos=agendamentos)

# Rota para adicionar um novo agendamento
@agendamento_bp.route('/novo', methods=['GET', 'POST'])
def adicionar_agendamento():
    pacientes = Paciente.query.all()
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data_horario = request.form['data_horario']
        status = request.form.get('status', 'Pendente')

        novo_agendamento = Agendamento(
            paciente_id=paciente_id,
            data_horario=datetime.strptime(data_horario, '%Y-%m-%dT%H:%M'),
            status=status
        )

        try:
            db.session.add(novo_agendamento)
            db.session.commit()
            flash('Agendamento realizado com sucesso!', 'success')
            return redirect(url_for('agendamento.listar_agendamentos'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar agendamento: {str(e)}', 'error')
            return redirect(url_for('agendamento.adicionar_agendamento'))

    return render_template('adicionar_agendamentos.html', pacientes=pacientes)

# Rota para editar um agendamento
@agendamento_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        agendamento.paciente_id = request.form['paciente_id']
        agendamento.data_horario = datetime.strptime(request.form['data_horario'], '%Y-%m-%dT%H:%M')
        agendamento.status = request.form.get('status', 'Pendente')

        try:
            db.session.commit()
            flash('Agendamento atualizado com sucesso!', 'success')
            return redirect(url_for('agendamento.listar_agendamentos'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar agendamento: {str(e)}', 'error')
            return redirect(url_for('agendamento.editar_agendamento', id=id))

    return render_template('editar_agendamento.html', agendamento=agendamento, pacientes=pacientes)

# Rota para deletar um agendamento
@agendamento_bp.route('/<int:id>/deletar', methods=['POST'])
def deletar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    try:
        db.session.delete(agendamento)
        db.session.commit()
        flash('Agendamento deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar agendamento: {str(e)}', 'error')

    return redirect(url_for('agendamento.listar_agendamentos'))