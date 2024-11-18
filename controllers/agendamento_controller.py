from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Agendamento, Paciente
from datetime import datetime

agendamento_bp = Blueprint('agendamento', __name__, url_prefix='/agendamentos')

# Rota para listar agendamentos
@agendamento_bp.route('/')
def listar_agendamentos():
    agendamentos = Agendamento.query.order_by(Agendamento.data_horario.asc()).all()
    return render_template('listar_agendamentos.html', agendamentos=agendamentos)

# Rota para adicionar um novo agendamento
@agendamento_bp.route('/novo', methods=['GET', 'POST'])
def adicionar_agendamento():
    pacientes = Paciente.query.all()
    if request.method == 'POST':
        data_horario = request.form['data_horario']
        paciente_id = request.form['paciente_id']
        status = request.form.get('status', 'Pendente')

        try:
            # Ajusta a conversão da data para o formato correto
            data_horario = datetime.strptime(data_horario, '%Y-%m-%dT%H:%M')

            novo_agendamento = Agendamento(
                data_horario=data_horario,
                paciente_id=paciente_id,
                status=status
            )

            db.session.add(novo_agendamento)
            db.session.commit()
            flash('Agendamento adicionado com sucesso!', 'success')
            return redirect(url_for('agendamento.listar_agendamentos'))
        except ValueError:
            flash('Formato de data inválido. Por favor, verifique o formato.', 'error')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar agendamento: {str(e)}', 'error')

    return render_template('adicionar_agendamento.html', pacientes=pacientes)

# Rota para editar um agendamento
@agendamento_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    pacientes = Paciente.query.all()

    if request.method == 'POST':
        data_horario = request.form['data_horario']
        paciente_id = request.form['paciente_id']
        status = request.form.get('status', 'Pendente')

        try:
            # Ajusta a conversão da data para o formato correto
            agendamento.data_horario = datetime.strptime(data_horario, '%Y-%m-%dT%H:%M')  # Adiciona o formato com "T"

            agendamento.paciente_id = paciente_id
            agendamento.status = status

            db.session.commit()
            flash('Agendamento atualizado com sucesso!', 'success')
            return redirect(url_for('agendamento.listar_agendamentos'))
        except ValueError:
            flash('Formato de data inválido. Por favor, verifique o formato.', 'error')
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar agendamento: {str(e)}', 'error')

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
