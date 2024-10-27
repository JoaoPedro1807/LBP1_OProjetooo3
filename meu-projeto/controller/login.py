from flask import Blueprint, render_template, request, redirect, url_for, flash
from model import users, sessoes

c = Blueprint('login', __name__)

@c.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if not sessoes.existe('nome'):
            return render_template('login.html')
        return redirect(url_for('index'))

    nome = request.form['nome']
    senha = request.form['senha']

    for u in users.Users:
        if nome == u.nome and senha == u.senha:
            sessoes.atualizar_login('nome', nome)
            sessoes.atualizar_login('tipo', u.tipo)
            return redirect(url_for('index'))

    flash('Credenciais incorretas.', 'warning')
    return redirect(url_for('login.login'))

@c.route('/logout')
def logout():
    sessoes.limpar_login()
    return redirect(url_for('index'))
