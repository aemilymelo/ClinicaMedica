from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Consulta, Agendamento

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

# Rota para listar consultas
@consulta_bp.route('/')
def listar_consultas():
    consultas = Consulta.query.all()
    return render_template('listar_consultas.html', consultas=consultas)

# Rota para registrar uma consulta
@consulta_bp.route('/novo', methods=['GET', 'POST'])
def registrar_consulta():
    agendamentos = Agendamento.query.filter(Agendamento.status == 'Realizado').all()
    if request.method == 'POST':
        agendamento_id = request.form['agendamento_id']
        diagnostico = request.form['diagnostico']
        prescricoes = request.form['prescricoes']

        nova_consulta = Consulta(
            agendamento_id=agendamento_id,
            diagnostico=diagnostico,
            prescricoes=prescricoes
        )

        try:
            db.session.add(nova_consulta)
            db.session.commit()
            flash('Consulta registrada com sucesso!', 'success')
            return redirect(url_for('consulta.listar_consultas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao registrar consulta: {str(e)}', 'error')

    return render_template('registrar_consulta.html', agendamentos=agendamentos)

# Rota para editar uma consulta
@consulta_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    if request.method == 'POST':
        consulta.diagnostico = request.form['diagnostico']
        consulta.prescricoes = request.form['prescricoes']

        try:
            db.session.commit()
            flash('Consulta atualizada com sucesso!', 'success')
            return redirect(url_for('consulta.listar_consultas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar consulta: {str(e)}', 'error')

    return render_template('editar_consulta.html', consulta=consulta)
