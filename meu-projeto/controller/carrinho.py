from flask import Blueprint, redirect, url_for, make_response, flash, request
from model import produto

c = Blueprint('carrinho', __name__)

@c.route('/carrinho/add')
def add():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('index')))
    if id:
        cookie = request.cookies.get(f'produto_{id}')
        if cookie:
            resp.set_cookie(f'produto_{id}', str(int(cookie) + 1))
        else:
            resp.set_cookie(f'produto_{id}', "1")
    else:
        flash('ID do produto inválido.', 'warning')
    return resp

@c.route('/carrinho/del')
def delete():
    id = request.args.get('id')
    resp = make_response(redirect(url_for('index')))
    if id:
        cookie = request.cookies.get(f'produto_{id}')
        if cookie:
            if int(cookie) > 1:
                resp.set_cookie(f'produto_{id}', str(int(cookie) - 1))
            else:
                resp.set_cookie(f'produto_{id}', '', expires=0)
        else:
            flash('O produto não está no carrinho para ser removido.', 'warning')
    else:
        flash('ID do produto inválido.', 'warning')
    return resp
