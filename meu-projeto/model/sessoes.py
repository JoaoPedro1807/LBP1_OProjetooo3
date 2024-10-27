from flask import session

Campos = ['nome', 'tipo']

def existe(campo):
    return campo in session

def get(campo):
    return session.get(campo)

def atualizar_login(campo, valor):
    session[campo] = valor

def limpar_login():
    for campo in Campos:
        session.pop(campo, None)
