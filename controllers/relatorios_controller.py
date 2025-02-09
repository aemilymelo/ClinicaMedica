from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Relatorio 
from datetime import datetime

relatorio_bp = Blueprint('relatorio', __name__, url_prefix='/relatorios')

# Rota para listar relatórios
@relatorio_bp.route('/')
def listar_relatorios():
    relatorios = Relatorio.query.all()  
    return render_template('listar_relatorio.html', relatorios=relatorios)

# Rota para adicionar um novo relatório
@relatorio_bp.route('/novo', methods=['GET', 'POST'])
def adicionar_relatorio():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data_nascimento = request.form['data_nascimento']
        telefone = request.form.get('telefone')
        endereco = request.form.get('endereco')
        historico = request.form.get('historico')
        queixa = request.form.get('queixa')
        exames = request.form.get('exames')
        diagnostico = request.form.get('diagnostico')
        tratamento = request.form.get('tratamento')
        recomendacoes = request.form.get('recomendacoes')

        novo_relatorio = Relatorio(  # Usa "Relatorio" com R maiúsculo
            nome=nome,
            cpf=cpf,
            data_nascimento=datetime.strptime(data_nascimento, '%Y-%m-%d'),
            telefone=telefone,
            endereco=endereco,
            historico=historico,
            queixa=queixa,
            exames=exames,
            diagnostico=diagnostico,
            tratamento=tratamento,
            recomendacoes=recomendacoes
        )

        try:
            db.session.add(novo_relatorio)
            db.session.commit()
            flash('Relatório adicionado com sucesso!', 'success')
            return redirect(url_for('relatorio.listar_relatorios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar relatório: {str(e)}', 'error')

    return render_template('adicionar_relatorio.html')

# Rota para editar um relatório
@relatorio_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def atualizar_relatorio(id):
    try:
        relatorio = Relatorio.query.get_or_404(id)  # Retorna 404 se não encontrar

        if request.method == 'POST':
            relatorio.nome = request.form.get('nome', relatorio.nome)
            relatorio.cpf = request.form.get('cpf', relatorio.cpf)

            data_nascimento = request.form.get('data_nascimento')
            if data_nascimento:
                try:
                    relatorio.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
                except ValueError:
                    flash("Formato de data inválido! Use AAAA-MM-DD.", "error")
                    return render_template('editar_relatorio.html', relatorio=relatorio)

            relatorio.telefone = request.form.get('telefone', relatorio.telefone)
            relatorio.endereco = request.form.get('endereco', relatorio.endereco)
            relatorio.historico = request.form.get('historico', relatorio.historico)
            relatorio.queixa = request.form.get('queixa', relatorio.queixa)
            relatorio.exames = request.form.get('exames', relatorio.exames)
            relatorio.diagnostico = request.form.get('diagnostico', relatorio.diagnostico)
            relatorio.tratamento = request.form.get('tratamento', relatorio.tratamento)
            relatorio.recomendacoes = request.form.get('recomendacoes', relatorio.recomendacoes)

            db.session.commit()
            flash('Relatório atualizado com sucesso!', 'success')
            return redirect(url_for('relatorio.listar_relatorios'))

    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao buscar ou atualizar relatório: {str(e)}', 'error')
        return redirect(url_for('relatorio.listar_relatorios'))

    return render_template('editar_relatorio.html', relatorio=relatorio)

# Rota para deletar um relatório
@relatorio_bp.route('/<int:id>/deletar', methods=['POST'])
def deletar_relatorio(id):
    relatorio = Relatorio.query.get_or_404(id)  # Usa "Relatorio" com R maiúsculo
    try:
        db.session.delete(relatorio)
        db.session.commit()
        flash('Relatório deletado com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao deletar relatório: {str(e)}', 'error')

    return redirect(url_for('relatorio.listar_relatorios'))
